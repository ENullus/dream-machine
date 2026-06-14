const schema = window.__SCHEMA__ || {};

const btnGenerate      = document.getElementById("btn-generate");
const btnGenerateDials = document.getElementById("btn-generate-dials");
const btnRegenerate    = document.getElementById("btn-regenerate");
const vortex           = document.getElementById("vortex-overlay");
const outputShell      = document.getElementById("output-shell");
const narrativeEl      = document.getElementById("narrative");
const complexityLabel  = document.getElementById("complexity-label");
const cmSvg            = document.getElementById("cm-svg");
const cmIdle           = document.getElementById("cm-idle");
const cmHover          = document.getElementById("cm-hover");
const cmHoverRing      = document.getElementById("cm-hover-ring");
const cmHoverName      = document.getElementById("cm-hover-name");
const cmHoverVal       = document.getElementById("cm-hover-val");

const CX = 330, CY = 330;   // SVG centre
const SVG_NS = "http://www.w3.org/2000/svg";

// ── Ring definitions (inside → outside) ──────────────────────────────────
// Each ring has a 5° gap at its sectorStart so the ring label (at sectorStart−5°) is readable.
// sectorStart=275° → label at 270° (top)  → ENVIRONMENT
// sectorStart=5°   → label at 0°   (right) → SUBSISTENCE
// sectorStart=95°  → label at 90°  (bottom)→ KINSHIP
// sectorStart=185° → label at 180° (left)  → SOCIETY
const RINGS = [
  {
    name: 'ENVIRONMENT', color: '#00d9ff',
    innerR: 62, outerR: 102, sectorStart: 275,
    keys: ["AnnualMeanTemperature","MonthlyMeanPrecipitation","TemperatureConstancy",
           "PrecipitationConstancy","TemperaturePredictability","PrecipitationPredictability"]
  },
  {
    name: 'SUBSISTENCE', color: '#00d9ff',
    innerR: 108, outerR: 155, sectorStart: 5,
    keys: ["EA001","EA002","EA003","EA004","EA005","EA042","EA028","EA029"]
  },
  {
    name: 'KINSHIP', color: '#00d9ff',
    innerR: 161, outerR: 216, sectorStart: 95,
    keys: ["EA043","EA008","EA009","EA010","EA011","EA012","EA017","EA018","EA019","EA020"]
  },
  {
    name: 'SOCIETY', color: '#00d9ff',
    innerR: 222, outerR: 285, sectorStart: 185,
    keys: ["EA033","EA030","EA070","EA065","EA066","EA067","EA068","EA069","EA073","EA076"]
  }
];

// ── Geometry helpers ──────────────────────────────────────────────────────
function toRad(deg) { return deg * Math.PI / 180; }

function annularSector(innerR, outerR, startDeg, endDeg) {
  if (Math.abs(endDeg - startDeg) < 0.05) return "";
  const s = toRad(startDeg), e = toRad(endDeg);
  const sweep = endDeg - startDeg;
  const large = sweep > 180 ? 1 : 0;
  const xi1 = CX + innerR * Math.cos(s), yi1 = CY + innerR * Math.sin(s);
  const xi2 = CX + innerR * Math.cos(e), yi2 = CY + innerR * Math.sin(e);
  const xo1 = CX + outerR * Math.cos(s), yo1 = CY + outerR * Math.sin(s);
  const xo2 = CX + outerR * Math.cos(e), yo2 = CY + outerR * Math.sin(e);
  return `M${f(xi1)},${f(yi1)} A${innerR},${innerR} 0 ${large} 1 ${f(xi2)},${f(yi2)} L${f(xo2)},${f(yo2)} A${outerR},${outerR} 0 ${large} 0 ${f(xo1)},${f(yo1)} Z`;
}

function f(n) { return n.toFixed(2); }

// ── Global drag state ─────────────────────────────────────────────────────
let activeSector = null;

cmSvg.addEventListener("mousemove", e => {
  if (!activeSector) return;
  activeSector.onDrag(e);
});
document.addEventListener("mouseup", () => { activeSector = null; cmSvg.style.cursor = ''; });
cmSvg.addEventListener("touchmove", e => {
  if (!activeSector) return;
  activeSector.onDrag(e);
  e.preventDefault();
}, { passive: false });
document.addEventListener("touchend", () => { activeSector = null; });

function svgAngle(e) {
  const rect = cmSvg.getBoundingClientRect();
  const sx = 660 / rect.width, sy = 660 / rect.height;
  const cx = e.touches ? e.touches[0].clientX : e.clientX;
  const cy2 = e.touches ? e.touches[0].clientY : e.clientY;
  let deg = Math.atan2((cy2 - rect.top) * sy - CY, (cx - rect.left) * sx - CX) * 180 / Math.PI;
  if (deg < 0) deg += 360;
  return deg;
}

// ── Build rings ────────────────────────────────────────────────────────────
function buildRing(ring) {
  const keys = ring.keys.filter(k => schema[k]);
  if (!keys.length) return;

  const n = keys.length;
  const nominalAngle = 360 / n;      // degrees per sector (including gap)
  const sectorGap    = 2;            // degrees between sectors
  const fillSpan     = nominalAngle - sectorGap; // effective fill degrees

  keys.forEach((key, i) => {
    const info = schema[key];
    const startDeg = ring.sectorStart + i * nominalAngle;
    const endDeg   = startDeg + fillSpan;

    // Background (track) sector
    const bgEl = document.createElementNS(SVG_NS, "path");
    bgEl.setAttribute("d", annularSector(ring.innerR, ring.outerR, startDeg, endDeg));
    bgEl.setAttribute("fill", "rgba(0,0,0,0.45)");
    bgEl.setAttribute("stroke", "rgba(0,217,255,0.18)");
    bgEl.setAttribute("stroke-width", "0.5");
    bgEl.style.cursor = "pointer";
    cmSvg.appendChild(bgEl);

    // Fill sector (value)
    const fillEl = document.createElementNS(SVG_NS, "path");
    fillEl.setAttribute("fill", "rgba(0,217,255,0.28)");
    fillEl.setAttribute("stroke", "#00d9ff");
    fillEl.setAttribute("stroke-width", "0.8");
    fillEl.style.cssText = "cursor:pointer;filter:drop-shadow(0 0 4px rgba(0,217,255,0.6))";
    cmSvg.appendChild(fillEl);

    // Hidden input
    const input = document.createElement("input");
    input.type = "hidden";
    input.dataset.var = key;
    if (info.type === "categorical") {
      input.dataset.validValues = JSON.stringify(info.valid_values || []);
      input.dataset.labels      = JSON.stringify(info.labels      || {});
    }
    document.getElementById("cm-machine").appendChild(input);

    // Value state
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

    function updateFill(raw) {
      const val = Math.max(minV, Math.min(maxV, Math.round(raw / step) * step));
      input.value = val;
      const t = maxV > minV ? (val - minV) / (maxV - minV) : 0;
      const usedDeg = t * fillSpan;
      fillEl.setAttribute("d", usedDeg > 0.2 ? annularSector(ring.innerR, ring.outerR, startDeg, startDeg + usedDeg) : "");
      // Update hover display if this sector is hovered
      if (cmHover.style.display !== "none" && cmHoverName.textContent === (info.name || key)) {
        cmHoverVal.textContent = formatValue(input, info);
      }
    }

    const initVal = info.type === "categorical" ? (info.valid_values?.[0] ?? minV) : minV;
    updateFill(initVal);

    input.addEventListener("change", () => updateFill(parseFloat(input.value)));

    // Drag handler: angle within the sector maps to value
    function onDrag(e) {
      const angle = svgAngle(e);
      let rel = ((angle - startDeg) % 360 + 360) % 360;
      if (rel > fillSpan + 30) rel = 0;
      else if (rel > fillSpan) rel = fillSpan;
      updateFill(minV + (rel / fillSpan) * (maxV - minV));
    }

    function showHover() {
      cmIdle.style.display  = "none";
      cmHover.style.display = "block";
      cmHoverRing.textContent = ring.name;
      cmHoverName.textContent = info.name || key;
      cmHoverVal.textContent  = formatValue(input, info);
    }

    function hideHover() {
      cmIdle.style.display  = "block";
      cmHover.style.display = "none";
    }

    [bgEl, fillEl].forEach(el => {
      el.addEventListener("mouseenter", showHover);
      el.addEventListener("mouseleave", () => { if (!activeSector) hideHover(); });
      el.addEventListener("mousedown", ev => {
        activeSector = { onDrag, showHover };
        cmSvg.style.cursor = "grabbing";
        onDrag(ev);
        showHover();
        ev.preventDefault();
      });
      el.addEventListener("touchstart", ev => {
        activeSector = { onDrag, showHover };
        onDrag(ev);
        showHover();
        ev.preventDefault();
      }, { passive: false });
    });
  });
}

// ── Inputs wiring ──────────────────────────────────────────────────────────
function buildInputs() {
  RINGS.forEach(buildRing);
}

function getInputs() {
  const values = {};
  document.querySelectorAll("[data-var]").forEach(el => {
    const key = el.dataset.var, info = schema[key];
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

// ── Output reveal ─────────────────────────────────────────────────────────
function revealOutput(data) {
  narrativeEl.textContent = data.description || "No narrative generated.";
  if (complexityLabel && data.complexity !== undefined) {
    complexityLabel.textContent = `COMPLEXITY INDEX: ${data.complexity.toFixed(2)}`;
  }
  outputShell.classList.remove("intro-locked");
  outputShell.classList.add("reveal");
  setTimeout(() => outputShell.scrollIntoView({ behavior: "smooth", block: "start" }), 200);
}

// ── API calls ─────────────────────────────────────────────────────────────
async function generate() {
  showVortex(true);
  const res  = await fetch("/generate", { method: "POST", headers: { "Content-Type": "application/json" }, body: "{}" });
  const data = await res.json();
  showVortex(false);
  if (!res.ok) return;
  setInputs(data.society || {});
  setTimeout(() => revealOutput(data), 400);
}

async function generateFromDials() {
  showVortex(true);
  const payload = getInputs();
  const res  = await fetch("/predict", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) });
  const data = await res.json();
  showVortex(false);
  if (!res.ok) return;
  setTimeout(() => revealOutput(data), 400);
}

// ── Helpers ───────────────────────────────────────────────────────────────
function formatValue(input, info) {
  if (info.type === "categorical") {
    const labels = JSON.parse(input.dataset.labels || "{}");
    const val    = parseInt(input.value, 10);
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
