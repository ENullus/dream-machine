import os
os.environ['__NV_PRIME_RENDER_OFFLOAD'] = '1'
os.environ['__GLX_VENDOR_LIBRARY_NAME'] = 'nvidia'

import pygame
import moderngl
import numpy as np
import math
import sys
import ctypes
import subprocess
import time as _time


class HyperdimensionalIllusion:
    def __init__(self, fullscreen=False):
        pygame.init()

        self.is_fullscreen = fullscreen
        if fullscreen:
            info = pygame.display.Info()
            self.screen_width = info.current_w
            self.screen_height = info.current_h
            self.screen = pygame.display.set_mode(
                (self.screen_width, self.screen_height),
                pygame.OPENGL | pygame.DOUBLEBUF | pygame.FULLSCREEN,
            )
        else:
            self.screen_width = 1600
            self.screen_height = 900
            self.screen = pygame.display.set_mode(
                (self.screen_width, self.screen_height),
                pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE,
            )

        pygame.display.set_caption("Hyperdimensional Illusion")
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)

        self.ctx = moderngl.create_context()
        print(f"GPU: {self.ctx.info['GL_RENDERER']}")
        print(f"GL:  {self.ctx.info['GL_VERSION']}")

        dw, dh = self._get_drawable_size()
        print(f"Window: {self.screen_width}x{self.screen_height}  Drawable: {dw}x{dh}")

        # camera: 3D position + W (4th dimension)
        self.cam_pos = np.array([0.1, 0.3, 0.1], dtype=np.float32)
        self.cam_w = 0.0
        self.cam_yaw = 0.0
        self.cam_pitch = 0.0

        self.base_speed = 0.03
        self.mouse_sens = 0.002
        self.w_drift = 0.005       # very slow deliberate descent
        self.mandelbulb_power = 8.0

        self.velocity = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        self.cam_roll = 0.0
        self.move_drag = 2.0       # exponential drag (lower = more coast)
        self.move_accel = 35.0     # acceleration multiplier on base_speed

        self.recording = False
        self.ffmpeg_proc = None
        self.record_path = os.path.join(
            os.path.dirname(__file__) or '.', 'hyperdimensional_recording.mp4'
        )

        self._load_shader()
        self._make_quad()
        self.clock = pygame.time.Clock()

        print("\n  HYPERDIMENSIONAL ILLUSION")
        print("  ========================")
        print("  WASD          move")
        print("  mouse         look")
        print("  shift         fast")
        print("  space / ctrl  up / down")
        print("  Q / E         shift through 4th dimension")
        print("  up / down     morph power")
        print("  +  / -        speed up / slow down")
        print("  F             fullscreen")
        print("  F2            start/stop recording")
        print("  R             reset")
        print("  ESC           quit\n")

    def _get_drawable_size(self):
        """Get actual GL drawable size via SDL2 (handles HiDPI/scaling correctly)."""
        try:
            sdl2 = ctypes.CDLL('libSDL2-2.0.so.0')
            info = pygame.display.get_wm_info()
            window = info.get('window', 0)
            w, h = ctypes.c_int(0), ctypes.c_int(0)
            sdl2.SDL_GL_GetDrawableSize(ctypes.c_void_p(window), ctypes.byref(w), ctypes.byref(h))
            if w.value > 0 and h.value > 0:
                return w.value, h.value
        except Exception:
            pass
        return self.screen_width, self.screen_height

    # ----------------------------------------------------------------
    # recording
    # ----------------------------------------------------------------

    def start_recording(self):
        w, h = self._get_drawable_size()
        cmd = [
            'ffmpeg', '-y',
            '-f', 'rawvideo',
            '-pix_fmt', 'rgb24',
            '-s', f'{w}x{h}',
            '-r', '45',
            '-i', 'pipe:0',
            '-vf', 'vflip',
            '-c:v', 'libx264',
            '-preset', 'fast',
            '-crf', '18',
            '-pix_fmt', 'yuv420p',
            self.record_path,
        ]
        try:
            self.ffmpeg_proc = subprocess.Popen(
                cmd, stdin=subprocess.PIPE,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            self.recording = True
            self.record_res = (w, h)
            print(f"\n  RECORDING {w}x{h} -> {self.record_path}")
        except FileNotFoundError:
            print("\n  ffmpeg not found -- install with: sudo apt install ffmpeg")

    def stop_recording(self):
        if self.ffmpeg_proc:
            try:
                self.ffmpeg_proc.stdin.close()
            except Exception:
                pass
            self.ffmpeg_proc.wait()
            self.ffmpeg_proc = None
        self.recording = False
        print(f"\n  RECORDING SAVED -> {self.record_path}")

    def capture_frame(self):
        if not self.recording or not self.ffmpeg_proc:
            return
        try:
            w, h = self.record_res
            data = self.ctx.fbo.read(viewport=(0, 0, w, h), components=3)
            self.ffmpeg_proc.stdin.write(data)
        except BrokenPipeError:
            self.recording = False
            self.ffmpeg_proc = None
            print("\n  recording pipe broke -- stopped")

    # ----------------------------------------------------------------

    def _load_shader(self):
        vert = "#version 330\nin vec2 in_position;\nvoid main(){gl_Position=vec4(in_position,0,1);}"

        shader_path = os.path.join(os.path.dirname(__file__) or '.', 'hyperdimensional_illusion.glsl')
        try:
            with open(shader_path) as f:
                frag = f.read()
        except FileNotFoundError:
            print(f"Shader not found: {shader_path}")
            sys.exit(1)

        self.prog = self.ctx.program(vertex_shader=vert, fragment_shader=frag)

    def _make_quad(self):
        verts = np.array([-1, -1, 1, -1, -1, 1, 1, 1], dtype='f4')
        vbo = self.ctx.buffer(verts)
        self.vao = self.ctx.simple_vertex_array(self.prog, vbo, 'in_position')

    # ----------------------------------------------------------------

    def _forward(self):
        sy, cy = math.sin(self.cam_yaw), math.cos(self.cam_yaw)
        sp, cp = math.sin(self.cam_pitch), math.cos(self.cam_pitch)
        return np.array([sy * cp, sp, cy * cp], dtype=np.float32)

    def _right(self):
        sy, cy = math.sin(self.cam_yaw), math.cos(self.cam_yaw)
        return np.array([cy, 0.0, -sy], dtype=np.float32)

    def _target(self):
        return self.cam_pos + self._forward()

    def handle_input(self, dt):
        keys = pygame.key.get_pressed()

        fast = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        fwd = self._forward()
        rgt = self._right()

        wish = np.zeros(3, dtype=np.float32)
        if keys[pygame.K_w]: wish += fwd
        if keys[pygame.K_s]: wish -= fwd
        if keys[pygame.K_d]: wish += rgt
        if keys[pygame.K_a]: wish -= rgt
        if keys[pygame.K_SPACE]: wish[1] += 1.0
        if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]: wish[1] -= 1.0

        norm = np.linalg.norm(wish)
        if norm > 0.001:
            wish /= norm

        accel = self.base_speed * self.move_accel * (2.5 if fast else 1.0)
        self.velocity += wish * accel * dt
        self.velocity *= math.exp(-self.move_drag * dt)
        self.cam_pos += self.velocity * dt

        # roll: lean into lateral movement (trying not to fall)
        lateral_v = float(np.dot(self.velocity, rgt))
        up_v = self.velocity[1]
        roll_target = np.clip(-lateral_v * 0.18 + up_v * 0.06, -0.22, 0.22)
        self.cam_roll += (roll_target - self.cam_roll) * min(1.0, 2.5 * dt)

        # 4th dimension
        if keys[pygame.K_q]: self.cam_w -= dt * 0.5
        if keys[pygame.K_e]: self.cam_w += dt * 0.5
        self.cam_w += dt * self.w_drift

        # power morph
        if keys[pygame.K_UP]:
            self.mandelbulb_power = min(self.mandelbulb_power + 0.03, 14.0)
        if keys[pygame.K_DOWN]:
            self.mandelbulb_power = max(self.mandelbulb_power - 0.03, 3.0)

        # speed control
        if keys[pygame.K_EQUALS] or keys[pygame.K_PLUS] or keys[pygame.K_KP_PLUS]:
            self.base_speed = min(self.base_speed * 1.02, 1.0)
        if keys[pygame.K_MINUS] or keys[pygame.K_KP_MINUS]:
            self.base_speed = max(self.base_speed * 0.98, 0.005)

    # ----------------------------------------------------------------

    def toggle_fullscreen(self):
        pygame.display.toggle_fullscreen()
        self.is_fullscreen = not self.is_fullscreen
        info = pygame.display.Info()
        self.screen_width = info.current_w if self.is_fullscreen else 1600
        self.screen_height = info.current_h if self.is_fullscreen else 900

    # ----------------------------------------------------------------

    def render(self, t):
        w, h = self._get_drawable_size()
        self.ctx.fbo.viewport = (0, 0, w, h)
        self.ctx.clear(0.82, 0.84, 0.88, 1.0)

        def _set(name, val):
            if name in self.prog:
                self.prog[name].value = val

        idle_sway = math.sin(t * 0.3) * 0.012 + math.sin(t * 0.17) * 0.008
        final_roll = self.cam_roll + idle_sway

        _set('iResolution', (float(w), float(h), 0.0))
        _set('iTime', t)
        _set('cameraPosition', tuple(self.cam_pos.tolist()))
        _set('cameraTarget', tuple(self._target().tolist()))
        _set('cameraRoll', final_roll)
        _set('mandelbulbPower', self.mandelbulb_power)
        _set('cameraW', self.cam_w)

        self.vao.render(moderngl.TRIANGLE_STRIP)

    # ----------------------------------------------------------------

    def run(self):
        running = True
        t = 0.0
        status_t = 0.0
        pygame.mouse.set_pos(self.screen_width // 2, self.screen_height // 2)

        while running:
            dt = self.clock.tick(45) / 1000.0
            t += dt
            status_t += dt

            if status_t > 0.6:
                p = self.cam_pos
                rec = " [REC]" if self.recording else ""
                print(
                    f"\r  pos ({p[0]:+.1f} {p[1]:+.1f} {p[2]:+.1f})  "
                    f"W {self.cam_w:+.2f}  "
                    f"pow {self.mandelbulb_power:.1f}  "
                    f"spd {self.base_speed:.3f}{rec}   ",
                    end="", flush=True,
                )
                status_t = 0.0

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    running = False
                elif ev.type == pygame.VIDEORESIZE:
                    self.screen_width = ev.w
                    self.screen_height = ev.h
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        running = False
                    elif ev.key == pygame.K_f:
                        self.toggle_fullscreen()
                    elif ev.key == pygame.K_F2:
                        if self.recording:
                            self.stop_recording()
                        else:
                            self.start_recording()
                    elif ev.key == pygame.K_r:
                        self.cam_pos[:] = [0.1, 0.3, 0.1]
                        self.velocity[:] = [0.0, 0.0, 0.0]
                        self.cam_yaw = self.cam_pitch = 0.0
                        self.cam_roll = 0.0
                        self.cam_w = 0.0
                        print("\n  reset to origin")
                elif ev.type == pygame.MOUSEWHEEL:
                    self.base_speed *= 1.15 if ev.y > 0 else 0.87
                    self.base_speed = max(0.005, min(1.0, self.base_speed))
                elif ev.type == pygame.MOUSEMOTION:
                    dx, dy = ev.rel
                    self.cam_yaw += dx * self.mouse_sens
                    self.cam_pitch -= dy * self.mouse_sens
                    self.cam_pitch = max(-1.5, min(1.5, self.cam_pitch))

            self.handle_input(dt)
            self.render(t)
            self.capture_frame()
            pygame.display.flip()

        if self.recording:
            self.stop_recording()
        print("\n")
        pygame.quit()


if __name__ == '__main__':
    HyperdimensionalIllusion(fullscreen=False).run()
