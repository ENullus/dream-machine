const reportText = document.getElementById("report-text");
const btnBack = document.getElementById("btn-back");
const btnRegenerate = document.getElementById("btn-regenerate");
const btnVoice = document.getElementById("btn-voice-report");
const vortex = document.getElementById("vortex-overlay");
const reportShell = document.querySelector(".report-shell");

let voiceEnabled = false;
let currentSpeech = null;

function showVortex(on) {
  if (!vortex) return;
  if (on) {
    const inner = vortex.innerHTML;
    vortex.innerHTML = inner;
    vortex.classList.remove("hidden");
    requestAnimationFrame(() => vortex.classList.add("active"));
  } else {
    vortex.classList.remove("active");
    setTimeout(() => vortex.classList.add("hidden"), 500);
  }
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

function loadReport() {
  const raw = sessionStorage.getItem("dream_report");
  if (!raw) {
    reportText.textContent = "No report found. Return to dials and generate.";
    return;
  }
  try {
    const data = JSON.parse(raw);
    reportText.textContent = data.description || "No narrative available.";
    if (voiceEnabled && data.description) {
      speak(data.description);
    }
  } catch (err) {
    reportText.textContent = "Report data corrupted. Return to dials and generate again.";
  }
}

async function regenerate() {
  showVortex(true);
  const res = await fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({}),
  });
  const data = await res.json();
  showVortex(false);
  if (!res.ok) {
    reportText.textContent = data.error || "Generation failed.";
    return;
  }
  sessionStorage.setItem("dream_report", JSON.stringify(data));
  loadReport();
}

btnBack.addEventListener("click", () => {
  window.location.href = "/";
});

btnRegenerate.addEventListener("click", regenerate);

btnVoice.addEventListener("click", () => {
  voiceEnabled = !voiceEnabled;
  btnVoice.textContent = `VOICE: ${voiceEnabled ? "ON" : "OFF"}`;
  loadReport();
});

function playIntro() {
  const transition = sessionStorage.getItem("dream_transition");
  if (transition === "vortex") {
    // Vortex carries over from index page
    showVortex(true);
    setTimeout(() => {
      showVortex(false);
      // After vortex fades, assemble the report panel
      setTimeout(() => {
        if (reportShell) {
          reportShell.classList.remove("intro-locked");
          reportShell.classList.add("reveal");
        }
      }, 400);
    }, 800);
  } else if (reportShell) {
    reportShell.classList.remove("intro-locked");
    reportShell.classList.add("reveal");
  }
  sessionStorage.removeItem("dream_transition");
}

playIntro();
loadReport();
