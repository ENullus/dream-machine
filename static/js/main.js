const schema = window.__SCHEMA__ || {};

const btnGenerate = document.getElementById("btn-generate");
const btnGenerateDials = document.getElementById("btn-generate-dials");
const btnVoice = document.getElementById("btn-voice");
const vortex = document.getElementById("vortex-overlay");

let voiceEnabled = false;
let currentSpeech = null;

const GROUPS = {
  subsistence: {
    container: "group-subsistence",
    keys: ["EA001","EA002","EA003","EA004","EA005","EA042","EA028","EA029"]
  },
  environment: {
    container: "group-environment",
    keys: ["AnnualMeanTemperature","MonthlyMeanPrecipitation","TemperatureConstancy","PrecipitationConstancy","TemperaturePredictability","PrecipitationPredictability"]
  },
  society: {
    container: "group-society",
    keys: ["EA033","EA030","EA070","EA065","EA066","EA067","EA068","EA069","EA073","EA076"]
  },
  kinship: {
    container: "group-kinship",
    keys: ["EA043","EA008","EA009","EA010","EA011","EA012","EA017","EA018","EA019","EA020"]
  }
};

function buildDial(key, info, container) {
  if (!info) return;

  const wrapper = document.createElement("div");
  wrapper.className = "dial";

  const label = document.createElement("label");
  label.textContent = info.name || key;
  wrapper.appendChild(label);

  const slider = document.createElement("div");
  slider.className = "lcars-slider";

  const track = document.createElement("div");
  track.className = "lcars-track";
  const fill = document.createElement("div");
  fill.className = "lcars-fill";
  track.appendChild(fill);
  slider.appendChild(track);

  const ticks = document.createElement("div");
  ticks.className = "lcars-ticks";
  const tickCount = info.type === "continuous" ? 10 : Math.min(
    info.type === "categorical" ? info.valid_values.length : (info.max - info.min + 1), 12
  );
  for (let i = 0; i < tickCount; i++) {
    const tick = document.createElement("div");
    tick.className = "lcars-tick";
    ticks.appendChild(tick);
  }
  slider.appendChild(ticks);

  const input = document.createElement("input");
  input.type = "range";
  if (info.type === "categorical") {
    input.min = Math.min(...info.valid_values);
    input.max = Math.max(...info.valid_values);
    input.step = 1;
    input.value = info.valid_values?.[0] ?? input.min;
    input.dataset.validValues = JSON.stringify(info.valid_values || []);
    input.dataset.labels = JSON.stringify(info.labels || {});
  } else {
    input.min = info.min ?? 0;
    input.max = info.max ?? 1;
    input.step = info.type === "continuous" ? 0.1 : 1;
    input.value = info.min ?? 0;
  }
  input.dataset.var = key;
  slider.appendChild(input);
  wrapper.appendChild(slider);

  const value = document.createElement("div");
  value.className = "value";
  value.textContent = formatValue(input, info);
  wrapper.appendChild(value);

  function updateFill() {
    const min = parseFloat(input.min);
    const max = parseFloat(input.max);
    const val = parseFloat(input.value);
    const pct = max > min ? ((val - min) / (max - min)) * 100 : 0;
    fill.style.width = pct + "%";
  }

  input.addEventListener("input", () => {
    if (info.type !== "continuous") {
      const n = parseInt(input.value, 10);
      if (!Number.isNaN(n)) input.value = Math.min(Math.max(n, parseInt(input.min), parseInt(input.max)));
    }
    value.textContent = formatValue(input, info);
    updateFill();
  });

  updateFill();
  container.appendChild(wrapper);
}

function buildInputs() {
  const placed = new Set();

  Object.entries(GROUPS).forEach(([, group]) => {
    const container = document.getElementById(group.container);
    if (!container) return;
    group.keys.forEach(key => {
      if (schema[key]) {
        buildDial(key, schema[key], container);
        placed.add(key);
      }
    });
  });

  // Any remaining keys go into society panel as fallback
  const fallback = document.getElementById("group-society");
  Object.entries(schema).forEach(([key, info]) => {
    if (!placed.has(key) && fallback) buildDial(key, info, fallback);
  });
}

function getInputs() {
  const values = {};
  document.querySelectorAll("[data-var]").forEach((el) => {
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
  document.querySelectorAll("[data-var]").forEach((el) => {
    const key = el.dataset.var;
    if (values[key] === undefined) return;
    el.value = values[key];
    const dial = el.closest(".dial");
    if (!dial) return;
    const valueEl = dial.querySelector(".value");
    if (valueEl) valueEl.textContent = formatValue(el, schema[key]);
    const fill = dial.querySelector(".lcars-fill");
    if (fill) {
      const min = parseFloat(el.min), max = parseFloat(el.max), val = parseFloat(el.value);
      fill.style.width = (max > min ? ((val - min) / (max - min)) * 100 : 0) + "%";
    }
  });
}

async function generate() {
  showVortex(true);
  const res = await fetch("/generate", { method: "POST", headers: { "Content-Type": "application/json" }, body: "{}" });
  const data = await res.json();
  if (!res.ok) { showVortex(false); return; }
  setInputs(data.society || {});
  sessionStorage.setItem("dream_report", JSON.stringify(data));
  sessionStorage.setItem("dream_transition", "vortex");
  setTimeout(() => { window.location.href = "/report"; }, 1200);
}

async function generateFromDials() {
  showVortex(true);
  const payload = getInputs();
  const res = await fetch("/predict", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) });
  const data = await res.json();
  if (!res.ok) { showVortex(false); return; }
  sessionStorage.setItem("dream_report", JSON.stringify(data));
  sessionStorage.setItem("dream_transition", "vortex");
  setTimeout(() => { window.location.href = "/report"; }, 1200);
}

function formatValue(input, info) {
  if (info.type === "categorical") {
    const labels = JSON.parse(input.dataset.labels || "{}");
    const val = parseInt(input.value, 10);
    return labels[val] || String(val);
  }
  return input.value;
}

function showVortex(on) {
  if (!vortex) return;
  if (on) {
    vortex.innerHTML = vortex.innerHTML;
    vortex.classList.remove("hidden");
    requestAnimationFrame(() => vortex.classList.add("active"));
  } else {
    vortex.classList.remove("active");
    setTimeout(() => vortex.classList.add("hidden"), 500);
  }
}

function speak(text) {
  if (!("speechSynthesis" in window)) return;
  if (currentSpeech) window.speechSynthesis.cancel();
  const utter = new SpeechSynthesisUtterance(text);
  utter.rate = 0.95; utter.pitch = 0.9;
  currentSpeech = utter;
  window.speechSynthesis.speak(utter);
}

btnGenerate.addEventListener("click", generate);
btnGenerateDials.addEventListener("click", generateFromDials);
btnVoice.addEventListener("click", () => {
  voiceEnabled = !voiceEnabled;
  btnVoice.textContent = `◎ VOICE: ${voiceEnabled ? "ON" : "OFF"}`;
});

buildInputs();
