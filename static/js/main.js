const schema = window.__SCHEMA__ || {};

const inputGrid = document.getElementById("input-grid");
const btnGenerate = document.getElementById("btn-generate");
const btnGenerateDials = document.getElementById("btn-generate-dials");
const btnVoice = document.getElementById("btn-voice");
const narrativeEl = document.getElementById("narrative");
const vortex = document.getElementById("vortex-overlay");
const outputPanel = document.getElementById("output-panel");

let voiceEnabled = false;
let currentSpeech = null;

function buildInputs() {
  Object.entries(schema).forEach(([key, info]) => {
    const wrapper = document.createElement("div");
    wrapper.className = "dial";

    const label = document.createElement("label");
    label.textContent = info.name || key;
    wrapper.appendChild(label);

    // LCARS slider container
    const slider = document.createElement("div");
    slider.className = "lcars-slider";

    const track = document.createElement("div");
    track.className = "lcars-track";
    const fill = document.createElement("div");
    fill.className = "lcars-fill";
    track.appendChild(fill);
    slider.appendChild(track);

    // Tick marks
    const ticks = document.createElement("div");
    ticks.className = "lcars-ticks";
    const tickCount = info.type === "continuous" ? 10 : Math.min(
      (info.type === "categorical" ? info.valid_values.length : (info.max - info.min + 1)),
      12
    );
    for (let i = 0; i < tickCount; i++) {
      const tick = document.createElement("div");
      tick.className = "lcars-tick";
      ticks.appendChild(tick);
    }
    slider.appendChild(ticks);

    // Native range input
    let input = document.createElement("input");
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

    // Value readout
    const value = document.createElement("div");
    value.className = "value";
    value.textContent = formatValue(input, info);
    wrapper.appendChild(value);

    // Update fill bar + value on input
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
        if (!Number.isNaN(n)) {
          const mn = parseInt(input.min, 10);
          const mx = parseInt(input.max, 10);
          input.value = Math.min(Math.max(n, mn), mx);
        }
      }
      value.textContent = formatValue(input, info);
      updateFill();
    });

    updateFill();

    // Stagger the dial appearance animation
    const idx = inputGrid.children.length;
    wrapper.style.animationDelay = (idx * 0.04) + "s";

    inputGrid.appendChild(wrapper);
  });
}

function getInputs() {
  const values = {};
  inputGrid.querySelectorAll("[data-var]").forEach((el) => {
    const key = el.dataset.var;
    const info = schema[key];
    if (info.type === "categorical") {
      values[key] = parseInt(el.value, 10);
    } else {
      values[key] = info.type === "continuous" ? parseFloat(el.value) : parseInt(el.value, 10);
    }
  });
  return values;
}

function setInputs(values) {
  inputGrid.querySelectorAll("[data-var]").forEach((el) => {
    const key = el.dataset.var;
    if (values[key] !== undefined) {
      el.value = values[key];
      // Update readout
      const dial = el.closest(".dial");
      if (dial) {
        const valueEl = dial.querySelector(".value");
        if (valueEl) valueEl.textContent = formatValue(el, schema[key]);
        // Update fill bar
        const fill = dial.querySelector(".lcars-fill");
        if (fill) {
          const min = parseFloat(el.min);
          const max = parseFloat(el.max);
          const val = parseFloat(el.value);
          const pct = max > min ? ((val - min) / (max - min)) * 100 : 0;
          fill.style.width = pct + "%";
        }
      }
    }
  });
}

async function generate() {
  showVortex(true);
  const res = await fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({}),
  });
  const data = await res.json();
  if (!res.ok) {
    showVortex(false);
    narrativeEl.textContent = data.error || "Generation failed.";
    return;
  }

  setInputs(data.society || {});
  sessionStorage.setItem("dream_report", JSON.stringify(data));
  sessionStorage.setItem("dream_transition", "vortex");
  // Keep vortex playing, then navigate
  setTimeout(() => { window.location.href = "/report"; }, 1200);
}

async function generateFromDials() {
  showVortex(true);
  const payload = getInputs();
  const res = await fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const data = await res.json();
  if (!res.ok) {
    showVortex(false);
    narrativeEl.textContent = data.error || "Generation failed.";
    if (data.errors && data.errors.length) {
      narrativeEl.textContent += "\n\n- " + data.errors.join("\n- ");
    }
    setTimeout(revealOutput, 300);
    return;
  }
  sessionStorage.setItem("dream_report", JSON.stringify(data));
  sessionStorage.setItem("dream_transition", "vortex");
  // Keep vortex playing, then navigate
  setTimeout(() => { window.location.href = "/report"; }, 1200);
}

function formatValue(input, info) {
  if (info.type === "categorical") {
    const labels = JSON.parse(input.dataset.labels || "{}");
    const val = parseInt(input.value, 10);
    return labels[val] ? labels[val] : String(val);
  }
  return input.value;
}

function showVortex(on) {
  if (!vortex) return;
  if (on) {
    // Force animation restart by re-inserting children
    const inner = vortex.innerHTML;
    vortex.innerHTML = inner;
    vortex.classList.remove("hidden");
    requestAnimationFrame(() => vortex.classList.add("active"));
  } else {
    vortex.classList.remove("active");
    setTimeout(() => vortex.classList.add("hidden"), 500);
  }
}

function revealOutput() {
  if (!outputPanel) return;
  outputPanel.classList.add("open");
}

function speak(text) {
  if (!("speechSynthesis" in window)) return;
  if (currentSpeech) {
    window.speechSynthesis.cancel();
  }
  const utter = new SpeechSynthesisUtterance(text);
  utter.rate = 0.95;
  utter.pitch = 0.9;
  currentSpeech = utter;
  window.speechSynthesis.speak(utter);
}

btnGenerate.addEventListener("click", generate);
btnGenerateDials.addEventListener("click", generateFromDials);
btnVoice.addEventListener("click", () => {
  voiceEnabled = !voiceEnabled;
  btnVoice.textContent = `VOICE: ${voiceEnabled ? "ON" : "OFF"}`;
});

buildInputs();
