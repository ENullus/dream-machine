const schema = window.__SCHEMA__ || {};

const btnGenerate      = document.getElementById("btn-generate");
const btnGenerateDials = document.getElementById("btn-generate-dials");
const btnRegenerate    = document.getElementById("btn-regenerate");
const vortex           = document.getElementById("vortex-overlay");
const outputShell      = document.getElementById("output-shell");
const narrativeEl      = document.getElementById("narrative");
const complexityLabel  = document.getElementById("complexity-label");

// ── Radial machine layout ──────────────────────────────────────────────────
const RADIAL_CX = 330;
const RADIAL_CY = 330;

// 4 sections, each centred on a cardinal axis, spreading 80° either side of that axis.
// rings: [{r: radius, n: dials_in_this_ring}]
const SECTIONS = [
  {
    id: 'subsistence', centerAngle: 0, spread: 80,
    keys: ["EA001","EA002","EA003","EA004","EA005","EA042","EA028","EA029"],
    rings: [{ r: 142, n: 4 }, { r: 198, n: 4 }]
  },
  {
    id: 'environment', centerAngle: 270, spread: 80,
    keys: ["AnnualMeanTemperature","MonthlyMeanPrecipitation","TemperatureConstancy",
           "PrecipitationConstancy","TemperaturePredictability","PrecipitationPredictability"],
    rings: [{ r: 142, n: 3 }, { r: 198, n: 3 }]
  },
  {
    id: 'society', centerAngle: 90, spread: 80,
    keys: ["EA033","EA030","EA070","EA065","EA066","EA067","EA068","EA069","EA073","EA076"],
    rings: [{ r: 142, n: 4 }, { r: 198, n: 3 }, { r: 252, n: 3 }]
  },
  {
    id: 'kinship', centerAngle: 180, spread: 80,
    keys: ["EA043","EA008","EA009","EA010","EA011","EA012","EA017","EA018","EA019","EA020"],
    rings: [{ r: 142, n: 4 }, { r: 198, n: 3 }, { r: 252, n: 3 }]
  }
];

// ── Circular sundial dial constants ────────────────────────────────────────
// Arc from 135° (7:30, bottom-left) clockwise 270° to 45° (4:30, bottom-right)
const DIAL_SIZE = 44;
const DIAL_R    = 14;
const DIAL_CX   = DIAL_SIZE / 2;
const DIAL_CY   = DIAL_SIZE / 2;
const ARC_START = 135;
const ARC_SWEEP = 270;
const SVG_NS = "http://www.w3.org/2000/svg";

function polarXY(deg, r) {
  const rad = deg * Math.PI / 180;
  return [DIAL_CX + r * Math.cos(rad), DIAL_CY + r * Math.sin(rad)];
}

function svgArcPath(startDeg, sweepDeg, r) {
  if (Math.abs(sweepDeg) < 0.5) return "";
  const endDeg = startDeg + sweepDeg;
  const [x1, y1] = polarXY(startDeg, r);
  const [x2, y2] = polarXY(endDeg, r);
  const largeArc = Math.abs(sweepDeg) > 180 ? 1 : 0;
  const sweepFlag = sweepDeg > 0 ? 1 : 0;
  return `M${x1.toFixed(2)},${y1.toFixed(2)} A${r},${r} 0 ${largeArc} ${sweepFlag} ${x2.toFixed(2)},${y2.toFixed(2)}`;
}

function valToArcAngle(val, minV, maxV) {
  const t = maxV > minV ? (val - minV) / (maxV - minV) : 0;
  return ARC_START + Math.max(0, Math.min(1, t)) * ARC_SWEEP;
}

function mouseAngleDeg(e, el) {
  const rect = el.getBoundingClientRect();
  const cx = rect.left + rect.width / 2;
  const cy = rect.top + rect.height / 2;
  const clientX = e.touches ? e.touches[0].clientX : e.clientX;
  const clientY = e.touches ? e.touches[0].clientY : e.clientY;
  let deg = Math.atan2(clientY - cy, clientX - cx) * 180 / Math.PI;
  if (deg < 0) deg += 360;
  return deg;
}

function buildDial(key, info, container, posX, posY) {
  if (!info) return;

  const wrapper = document.createElement("div");
  wrapper.className = "dial";
  // Absolute position within radial-machine, centred on the computed point
  wrapper.style.cssText = `position:absolute;left:${posX}px;top:${posY}px;transform:translate(-50%,-50%)`;

  const svg = document.createElementNS(SVG_NS, "svg");
  svg.setAttribute("viewBox", `0 0 ${DIAL_SIZE} ${DIAL_SIZE}`);
  svg.setAttribute("width", DIAL_SIZE);
  svg.setAttribute("height", DIAL_SIZE);
  svg.style.cssText = "overflow:visible;display:block;cursor:pointer;user-select:none;touch-action:none;-webkit-user-select:none";

  // Background circle
  const bg = document.createElementNS(SVG_NS, "circle");
  bg.setAttribute("cx", DIAL_CX); bg.setAttribute("cy", DIAL_CY); bg.setAttribute("r", DIAL_R + 4);
  bg.setAttribute("fill", "rgba(0,0,0,0.65)");
  bg.setAttribute("stroke", "rgba(0,217,255,0.14)");
  bg.setAttribute("stroke-width", "0.5");
  svg.appendChild(bg);

  // Track arc
  const track = document.createElementNS(SVG_NS, "path");
  track.setAttribute("d", svgArcPath(ARC_START, ARC_SWEEP, DIAL_R));
  track.setAttribute("fill", "none");
  track.setAttribute("stroke", "rgba(0,217,255,0.22)");
  track.setAttribute("stroke-width", "2");
  track.setAttribute("stroke-linecap", "round");
  svg.appendChild(track);

  // Fill arc
  const fillArc = document.createElementNS(SVG_NS, "path");
  fillArc.setAttribute("fill", "none");
  fillArc.setAttribute("stroke", "#00d9ff");
  fillArc.setAttribute("stroke-width", "2");
  fillArc.setAttribute("stroke-linecap", "round");
  fillArc.style.filter = "drop-shadow(0 0 3px rgba(0,217,255,1))";
  svg.appendChild(fillArc);

  // Tick marks (7 ticks)
  for (let i = 0; i <= 6; i++) {
    const tickAngle = ARC_START + (i / 6) * ARC_SWEEP;
    const isMajor = i % 3 === 0;
    const outer = DIAL_R + 5;
    const inner = outer - (isMajor ? 3 : 2);
    const [x1, y1] = polarXY(tickAngle, inner);
    const [x2, y2] = polarXY(tickAngle, outer);
    const tick = document.createElementNS(SVG_NS, "line");
    tick.setAttribute("x1", x1.toFixed(1)); tick.setAttribute("y1", y1.toFixed(1));
    tick.setAttribute("x2", x2.toFixed(1)); tick.setAttribute("y2", y2.toFixed(1));
    tick.setAttribute("stroke", isMajor ? "rgba(0,217,255,0.65)" : "rgba(0,217,255,0.28)");
    tick.setAttribute("stroke-width", isMajor ? "1" : "0.5");
    svg.appendChild(tick);
  }

  // Needle
  const needle = document.createElementNS(SVG_NS, "line");
  needle.setAttribute("stroke", "#00d9ff");
  needle.setAttribute("stroke-width", "1");
  needle.setAttribute("stroke-linecap", "round");
  needle.style.filter = "drop-shadow(0 0 2px rgba(0,217,255,1))";
  svg.appendChild(needle);

  // Center dot
  const dot = document.createElementNS(SVG_NS, "circle");
  dot.setAttribute("cx", DIAL_CX); dot.setAttribute("cy", DIAL_CY); dot.setAttribute("r", "2");
  dot.setAttribute("fill", "#00d9ff");
  dot.style.filter = "drop-shadow(0 0 3px rgba(0,217,255,1))";
  svg.appendChild(dot);

  wrapper.appendChild(svg);

  // Tooltip with name + value, shown on hover
  const tip = document.createElement("div");
  tip.className = "dial-tip";
  wrapper.appendChild(tip);

  // Hidden input carries the value
  const input = document.createElement("input");
  input.type = "hidden";
  input.dataset.var = key;
  if (info.type === "categorical") {
    input.dataset.validValues = JSON.stringify(info.valid_values || []);
    input.dataset.labels = JSON.stringify(info.labels || {});
  }
  wrapper.appendChild(input);

  let minV, maxV, step;
  if (info.type === "categorical") {
    minV = Math.min(...info.valid_values);
    maxV = Math.max(...info.valid_values);
    step = 1;
  } else {
    minV = info.min ?? 0;
    maxV = info.max ?? 1;
    step = info.type === "continuous" ? 0.1 : 1;
  }

  function updateVisuals(rawVal) {
    const val = Math.max(minV, Math.min(maxV, Math.round(rawVal / step) * step));
    input.value = val;
    const angle = valToArcAngle(val, minV, maxV);
    const used = angle - ARC_START;
    fillArc.setAttribute("d", used > 0.5 ? svgArcPath(ARC_START, used, DIAL_R) : "");
    const [nx, ny] = polarXY(angle, DIAL_R - 2);
    needle.setAttribute("x1", DIAL_CX); needle.setAttribute("y1", DIAL_CY);
    needle.setAttribute("x2", nx.toFixed(1)); needle.setAttribute("y2", ny.toFixed(1));
    const label = info.name || key;
    tip.textContent = `${label}: ${formatValue(input, info)}`;
  }

  const initVal = info.type === "categorical" ? (info.valid_values?.[0] ?? minV) : minV;
  updateVisuals(initVal);

  input.addEventListener("change", () => updateVisuals(parseFloat(input.value)));

  // Drag to rotate
  let dragging = false;

  function applyAngle(e) {
    const deg = mouseAngleDeg(e, svg);
    let rel = ((deg - ARC_START) % 360 + 360) % 360;
    if (rel > ARC_SWEEP + 45) rel = 0;
    else if (rel > ARC_SWEEP) rel = ARC_SWEEP;
    updateVisuals(minV + (rel / ARC_SWEEP) * (maxV - minV));
  }

  svg.addEventListener("mousedown", e => { dragging = true; applyAngle(e); e.preventDefault(); });
  window.addEventListener("mousemove", e => { if (dragging) applyAngle(e); });
  window.addEventListener("mouseup", () => { dragging = false; });
  svg.addEventListener("touchstart", e => { dragging = true; applyAngle(e); e.preventDefault(); }, { passive: false });
  svg.addEventListener("touchmove", e => { if (dragging) { applyAngle(e); e.preventDefault(); } }, { passive: false });
  svg.addEventListener("touchend", () => { dragging = false; });

  container.appendChild(wrapper);
}

function buildInputs() {
  const container = document.getElementById("radial-machine");
  if (!container) return;

  SECTIONS.forEach(section => {
    let keyIdx = 0;
    section.rings.forEach(ring => {
      for (let i = 0; i < ring.n; i++) {
        // Skip schema-missing keys
        while (keyIdx < section.keys.length && !schema[section.keys[keyIdx]]) keyIdx++;
        if (keyIdx >= section.keys.length) break;
        const key = section.keys[keyIdx++];

        // Compute polar position
        const startAng = section.centerAngle - section.spread / 2;
        const step = ring.n > 1 ? section.spread / (ring.n - 1) : 0;
        const angle = startAng + i * step;
        const rad = angle * Math.PI / 180;
        const x = RADIAL_CX + ring.r * Math.cos(rad);
        const y = RADIAL_CY + ring.r * Math.sin(rad);

        buildDial(key, schema[key], container, x, y);
      }
    });
  });
}

function getInputs() {
  const values = {};
  document.querySelectorAll("[data-var]").forEach(el => {
    const key = el.dataset.var;
    const info = schema[key];
    if (!info) return;
    values[key] = info.type === "categorical"
      ? parseInt(el.value, 10)
      : info.type === "continuous" ? parseFloat(el.value) : parseInt(el.value, 10);
  });
  return values;
}

function setInputs(values) {
  document.querySelectorAll("[data-var]").forEach(el => {
    const key = el.dataset.var;
    if (values[key] === undefined) return;
    el.value = values[key];
    el.dispatchEvent(new Event("change"));
  });
}

function revealOutput(data) {
  narrativeEl.textContent = data.description || "No narrative generated.";
  if (complexityLabel && data.complexity !== undefined) {
    complexityLabel.textContent = `COMPLEXITY INDEX: ${data.complexity.toFixed(2)}`;
  }
  outputShell.classList.remove("intro-locked");
  outputShell.classList.add("reveal");
  setTimeout(() => outputShell.scrollIntoView({ behavior: "smooth", block: "start" }), 200);
}

async function generate() {
  showVortex(true);
  const res = await fetch("/generate", { method: "POST", headers: { "Content-Type": "application/json" }, body: "{}" });
  const data = await res.json();
  showVortex(false);
  if (!res.ok) return;
  setInputs(data.society || {});
  setTimeout(() => revealOutput(data), 400);
}

async function generateFromDials() {
  showVortex(true);
  const payload = getInputs();
  const res = await fetch("/predict", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) });
  const data = await res.json();
  showVortex(false);
  if (!res.ok) return;
  setTimeout(() => revealOutput(data), 400);
}

function formatValue(input, info) {
  if (info.type === "categorical") {
    const labels = JSON.parse(input.dataset.labels || "{}");
    const val = parseInt(input.value, 10);
    return labels[val] || String(val);
  }
  const v = parseFloat(input.value);
  return isNaN(v) ? "—" : info.type === "continuous" ? v.toFixed(1) : String(Math.round(v));
}

function showVortex(on) {
  if (!vortex) return;
  if (on) {
    vortex.classList.remove("hidden");
    requestAnimationFrame(() => vortex.classList.add("active"));
  } else {
    vortex.classList.remove("active");
    setTimeout(() => vortex.classList.add("hidden"), 500);
  }
}

btnGenerate.addEventListener("click", generate);
btnGenerateDials.addEventListener("click", generateFromDials);
btnRegenerate.addEventListener("click", generate);

buildInputs();
