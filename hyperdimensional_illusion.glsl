#version 330 core

uniform vec3 iResolution;
uniform float iTime;
uniform vec3 cameraPosition;
uniform vec3 cameraTarget;
uniform float cameraRoll;
uniform float mandelbulbPower;
uniform float cameraW;

out vec4 fragColor;

const int MAX_STEPS = 150;
const float MIN_DIST = 0.0005;
const float MAX_DIST = 200.0;
const float CELL_SIZE = 25.0;

// ---------- 2D rotation ----------

mat2 rot2D(float a) {
    float c = cos(a), s = sin(a);
    return mat2(c, -s, s, c);
}

// ---------- infinite domain repetition ----------

vec3 cellRepeat(vec3 p, out vec3 cellId) {
    cellId = floor((p + CELL_SIZE * 0.5) / CELL_SIZE);
    return mod(p + CELL_SIZE * 0.5, CELL_SIZE) - CELL_SIZE * 0.5;
}

float cellHash(vec3 id) {
    return fract(sin(dot(id, vec3(12.9898, 78.233, 37.719))) * 43758.5453);
}

float cellHash2(vec3 id) {
    return fract(sin(dot(id, vec3(39.346, 11.135, 83.818))) * 43758.5453);
}

// ---------- spirit wisps: slow, ghostly, barely visible ----------

float spiritField(vec3 p, float t) {
    vec3 drift1 = vec3(sin(t * 0.025) * 0.15, cos(t * 0.03) * 0.1, sin(t * 0.02) * 0.18);
    vec3 drift2 = vec3(cos(t * 0.02) * 0.12, sin(t * 0.035) * 0.15, cos(t * 0.028) * 0.1);

    vec3 q1 = p * 0.15 + drift1 * t;
    float n1 = sin(q1.x * 2.3 + sin(q1.z * 1.1 + t * 0.05)) *
               sin(q1.y * 1.8 + sin(q1.x * 0.9 + t * 0.04)) *
               sin(q1.z * 2.0 + sin(q1.y * 1.3));

    vec3 q2 = p * 0.25 + drift2 * t;
    float n2 = sin(q2.x * 1.7 + sin(q2.z * 2.1 + t * 0.06)) *
               sin(q2.y * 2.5 + sin(q2.x * 1.6)) *
               sin(q2.z * 1.4 + sin(q2.y * 0.7 + t * 0.05));

    float n = max(abs(n1), abs(n2) * 0.8);
    return smoothstep(0.6, 0.92, n);
}

// ---------- smooth Mandelbox: 5 iterations, no turbulence ----------

float mandelboxCell(vec3 p, float cellW, float h, float h2) {
    p.xz *= rot2D(h * 6.28);
    p.xy *= rot2D(h2 * 6.28);

    vec4 z = vec4(p, cellW);
    vec4 c = z;
    float dr = 1.0;

    float foldLim = 1.0 + (h - 0.5) * 0.2;
    float minR2 = 0.25 + (h2 - 0.5) * 0.1;
    float fixR2 = 1.0;
    float scale = -1.5 - (mandelbulbPower - 3.0) * 0.055
                + (h2 - 0.5) * 0.3;

    for (int i = 0; i < 5; i++) {
        z = clamp(z, -foldLim, foldLim) * 2.0 - z;

        float r2 = dot(z, z);
        if (r2 < minR2) {
            float t = fixR2 / minR2;
            z *= t; dr *= t;
        } else if (r2 < fixR2) {
            float t = fixR2 / r2;
            z *= t; dr *= t;
        }

        z = z * scale + c;
        dr = dr * abs(scale) + 1.0;
    }

    return length(z) / abs(dr);
}

// ---------- distance estimator with W-driven descent zoom ----------

float DE(vec3 rawP) {
    float zoomScale = pow(2.5, cameraW * 0.15);
    vec3 zp = rawP / zoomScale;

    vec3 cellId;
    vec3 p = cellRepeat(zp, cellId);
    float h  = cellHash(cellId);
    float h2 = cellHash2(cellId);
    float cellW = cameraW * 0.3 + h * 4.0;

    return mandelboxCell(p, cellW, h, h2) * zoomScale;
}

// ---------- normal ----------

vec3 calcNormal(vec3 p) {
    vec2 e = vec2(0.0005, 0.0);
    return normalize(vec3(
        DE(p + e.xyy) - DE(p - e.xyy),
        DE(p + e.yxy) - DE(p - e.yxy),
        DE(p + e.yyx) - DE(p - e.yyx)
    ));
}

// ---------- color: ice / silver / pearl ----------

vec3 getColor(vec3 rawP, float steps) {
    float zoomScale = pow(2.5, cameraW * 0.15);
    vec3 zp = rawP / zoomScale;

    vec3 cellId;
    vec3 p = cellRepeat(zp, cellId);
    float h  = cellHash(cellId);
    float h2 = cellHash2(cellId);

    p.xz *= rot2D(h * 6.28);
    p.xy *= rot2D(h2 * 6.28);

    float cellW = cameraW * 0.3 + h * 4.0;

    vec4 z = vec4(p, cellW);
    vec4 c = z;

    float foldLim = 1.0 + (h - 0.5) * 0.2;
    float minR2 = 0.25 + (h2 - 0.5) * 0.1;
    float fixR2 = 1.0;
    float scale = -1.5 - (mandelbulbPower - 3.0) * 0.055
                + (h2 - 0.5) * 0.3;

    float trapXYZ = 1e10;
    float trapW = 1e10;
    float trapPlane = 1e10;
    float trapIter = 0.0;

    for (int i = 0; i < 5; i++) {
        z = clamp(z, -foldLim, foldLim) * 2.0 - z;

        float r2 = dot(z, z);
        if (r2 < minR2) { z *= fixR2 / minR2; }
        else if (r2 < fixR2) { z *= fixR2 / r2; }

        z = z * scale + c;

        float d = length(z.xyz);
        if (d < trapXYZ) {
            trapXYZ = d;
            trapIter = float(i);
        }
        trapW = min(trapW, abs(z.w));
        trapPlane = min(trapPlane, min(abs(z.x), min(abs(z.y), abs(z.z))));
    }

    float t1 = clamp(trapXYZ * 0.25, 0.0, 1.0);
    float t3 = clamp(trapPlane * 0.6, 0.0, 1.0);
    float ti = trapIter / 5.0;

    vec3 silver = vec3(0.82, 0.84, 0.87);
    vec3 ice    = vec3(0.62, 0.76, 0.90);
    vec3 pearl  = vec3(0.92, 0.90, 0.94);

    vec3 col = mix(ice, silver, t1);
    col = mix(col, pearl, smoothstep(0.2, 0.7, t3) * 0.5);

    // per-cell subtle tint
    float cellPhase = h * 6.28 + h2 * 3.14;
    col *= vec3(
        0.90 + 0.06 * sin(cellPhase),
        0.92 + 0.05 * sin(cellPhase + 1.5),
        0.95 + 0.05 * sin(cellPhase + 3.0)
    );

    // crease darkening
    float iterHeat = steps / float(MAX_STEPS);
    col *= 1.0 - iterHeat * 0.15;
    col = mix(col, vec3(0.45, 0.52, 0.65), iterHeat * 0.15);

    return col;
}

// ---------- ray march with spirit accumulation ----------

vec3 gSpiritGlow = vec3(0.0);

vec3 rayMarch(vec3 ro, vec3 rd) {
    gSpiritGlow = vec3(0.0);
    float depth = 0.0;
    float minD  = MAX_DIST;
    float steps = 0.0;

    for (int i = 0; i < MAX_STEPS; i++) {
        vec3 p = ro + rd * depth;
        float d = DE(p);
        minD = min(minD, d);
        steps = float(i);
        if (d < MIN_DIST) break;
        if (depth > MAX_DIST) break;

        float stepSize = d * 0.6;

        if (d > 0.1) {
            float sn = spiritField(p, iTime);
            if (sn > 0.01) {
                float fade = exp(-depth * 0.012);
                vec3 spiritCol = mix(vec3(0.50, 0.65, 0.90), vec3(0.72, 0.80, 1.0), sn);
                gSpiritGlow += sn * stepSize * spiritCol * fade * 0.04;
            }
        }

        depth += stepSize;
    }

    return vec3(depth, steps, (depth < MAX_DIST && minD < 0.005) ? 1.0 : 0.0);
}

// ---------- main ----------

void main() {
    vec2 uv = (gl_FragCoord.xy - 0.5 * iResolution.xy) / iResolution.y;

    vec3 ro = cameraPosition;
    vec3 ta = cameraTarget;

    vec3 ww = normalize(ta - ro);
    vec3 uu = normalize(cross(vec3(0, 1, 0), ww));
    vec3 vv = cross(ww, uu);
    float cr = cos(cameraRoll), sr = sin(cameraRoll);
    vec3 uu2 = cr * uu + sr * vv;
    vec3 vv2 = -sr * uu + cr * vv;
    vec3 rd = normalize(uv.x * uu2 + uv.y * vv2 + 0.75 * ww);

    vec3 res = rayMarch(ro, rd);
    float t     = res.x;
    float steps = res.y;
    float hit   = res.z;

    // background: featureless silver-white haze
    vec3 bgTop    = vec3(0.86, 0.88, 0.91);
    vec3 bgBottom = vec3(0.78, 0.80, 0.84);
    vec3 col = mix(bgBottom, bgTop, uv.y * 0.5 + 0.5);

    if (hit > 0.5) {
        vec3 pos = ro + rd * t;
        vec3 nor = calcNormal(pos);
        vec3 base = getColor(pos, steps);

        // clinical, flat, uncanny lighting
        vec3 l1 = normalize(vec3(0.3, 1.0, 0.2));
        vec3 l2 = normalize(vec3(-0.4, 0.3, -0.7));
        float d1 = clamp(dot(nor, l1), 0.0, 1.0);
        float d2 = clamp(dot(nor, l2), 0.0, 1.0) * 0.35;
        float amb = 0.45 + 0.10 * (nor.y * 0.5 + 0.5);

        float ao = 1.0 - steps / float(MAX_STEPS);
        ao = ao * ao * 0.7 + 0.3;

        col = base * (amb + d1 * 0.5 + d2) * ao;

        // faint cold rim
        float fres = pow(1.0 - abs(dot(nor, -rd)), 3.5);
        col += fres * vec3(0.55, 0.70, 0.95) * 0.2 * ao;

        // clean specular
        vec3 hv = normalize(l1 - rd);
        float spec = pow(max(dot(nor, hv), 0.0), 64.0) * 0.4;
        col += vec3(0.95, 0.95, 1.0) * spec * ao;

        // fog: dissolves into featureless white haze
        float fog = 1.0 - exp(-t * 0.008);
        vec3 fogCol = mix(bgBottom, bgTop, 0.6);
        col = mix(col, fogCol, fog);
    }

    // spirits: barely visible pale distortions
    col += gSpiritGlow;

    // tone map
    col = col / (0.85 + col);
    col = pow(col, vec3(0.97));

    // very subtle chromatic aberration
    float ab = length(uv) * 0.002;
    col.r = mix(col.r, col.g, ab);
    col.b = mix(col.b, col.g, -ab * 0.5);

    // gentle vignette
    col *= 1.0 - dot(uv, uv) * 0.1;

    fragColor = vec4(col, 1.0);
}
