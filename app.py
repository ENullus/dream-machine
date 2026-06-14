"""
Flask API for Society Dream Machine.

Endpoints:
  POST /generate  -> VAE generate + post-process + description + RF score
  POST /predict   -> RF score from provided inputs
"""

from __future__ import annotations

import json
import pickle
from typing import Any, Dict, List, Union, Optional, Tuple

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

from descriptions_mega import generate_full_description
from vae_postprocessor import fix_vae_output, validate_fixed_output
from variable_constraints import ALL_VARIABLES, RF_INPUT_VARS


class VAE(nn.Module):
    def __init__(self, input_dim: int, latent_dim: int = 20) -> None:
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
        )
        self.fc_mu = nn.Linear(64, latent_dim)
        self.fc_logvar = nn.Linear(64, latent_dim)
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, input_dim),
        )

    def encode(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        h = self.encoder(x)
        return self.fc_mu(h), self.fc_logvar(h)

    def reparameterize(self, mu: torch.Tensor, logvar: torch.Tensor) -> torch.Tensor:
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def decode(self, z: torch.Tensor) -> torch.Tensor:
        return self.decoder(z)

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        recon = self.decode(z)
        return recon, mu, logvar


app = Flask(__name__)
CORS(app)


def load_pickle(path: str):
    # Compatibility shim for pickles created with NumPy 2.x
    # which reference numpy._core in serialized objects.
    import sys
    import numpy as _np

    if "numpy._core" not in sys.modules:
        sys.modules["numpy._core"] = _np.core

    with open(path, "rb") as f:
        return pickle.load(f)


# Load models and metadata once at startup
vae_columns: List[str] = load_pickle("vae_columns.pkl")
vae_scaler = load_pickle("vae_scaler.pkl")
rf_model = load_pickle("dream_machine_model.pkl")
rf_inputs: List[str] = load_pickle("input_vars.pkl")

vae = VAE(input_dim=len(vae_columns), latent_dim=20)
vae.load_state_dict(torch.load("dream_machine_vae.pth", map_location="cpu"))
vae.eval()
torch.set_grad_enabled(False)

_fallback_mean: Optional[np.ndarray] = None
_fallback_scale: Optional[np.ndarray] = None


def build_fallback_scaler() -> Tuple[np.ndarray, np.ndarray]:
    df = pd.read_csv("MASTER_DATASET.csv", index_col=0)
    df = df[vae_columns].copy()
    for col in df.columns:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].median())
    mean = df.mean().to_numpy()
    scale = df.std(ddof=0).replace(0, 1).to_numpy()
    return mean, scale


def inverse_transform_fallback(values: np.ndarray) -> np.ndarray:
    global _fallback_mean, _fallback_scale
    if _fallback_mean is None or _fallback_scale is None:
        _fallback_mean, _fallback_scale = build_fallback_scaler()
    return values * _fallback_scale + _fallback_mean


def generate_society() -> Dict[str, Any]:
    z = torch.randn(1, 20)
    decoded = vae.decode(z).detach().numpy()
    if hasattr(vae_scaler, "inverse_transform"):
        raw = vae_scaler.inverse_transform(decoded)[0]
    else:
        raw = inverse_transform_fallback(decoded)[0]
    raw_dict = dict(zip(vae_columns, raw))
    fixed = fix_vae_output(raw_dict)
    return fixed


def predict_complexity(society: Dict[str, Any]) -> float:
    values = [society[var] for var in rf_inputs]
    pred = rf_model.predict([values])[0]
    return float(pred)


def to_jsonable(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(k): to_jsonable(v) for k, v in value.items()}
    if isinstance(value, list):
        return [to_jsonable(v) for v in value]
    if isinstance(value, tuple):
        return [to_jsonable(v) for v in value]
    if isinstance(value, (np.integer, np.floating)):
        return value.item()
    return value


@app.route("/generate", methods=["POST"])
def generate_endpoint():
    society = generate_society()
    is_valid, errors = validate_fixed_output(society)
    complexity = predict_complexity(society)
    description = generate_full_description(society)
    return jsonify(
        {
            "society": to_jsonable(society),
            "complexity": complexity,
            "description": description,
            "valid": is_valid,
            "errors": errors,
        }
    )


@app.route("/predict", methods=["POST"])
def predict_endpoint():
    payload = request.get_json(silent=True) or {}
    if not isinstance(payload, dict):
        return jsonify({"error": "Invalid JSON payload"}), 400

    missing = [var for var in rf_inputs if var not in payload]
    if missing:
        return jsonify({"error": "Missing inputs", "missing": missing}), 400

    try:
        society = {k: float(payload[k]) for k in payload}
    except (TypeError, ValueError):
        return jsonify({"error": "Inputs must be numeric"}), 400

    fixed = fix_vae_output(society)
    is_valid, errors = validate_fixed_output(fixed)
    if not is_valid:
        return jsonify({"error": "Invalid inputs", "errors": errors}), 400

    complexity = predict_complexity(fixed)
    description = generate_full_description(fixed)
    return jsonify(
        {
            "complexity": complexity,
            "society": to_jsonable(fixed),
            "description": description,
        }
    )


@app.route("/", methods=["GET"])
def index():
    friendly_names = {
        "EA001": "Gathering dependence",
        "EA002": "Hunting dependence",
        "EA003": "Fishing dependence",
        "EA004": "Herding dependence",
        "EA005": "Agriculture dependence",
        "AnnualMeanTemperature": "Annual mean temperature",
        "MonthlyMeanPrecipitation": "Monthly mean precipitation",
        "TemperatureConstancy": "Temperature constancy",
        "EA043": "Descent type",
        "EA009": "Marital composition",
        "EA012": "Marital residence",
        "EA042": "Dominant subsistence",
        "EA070": "Slavery",
        "EA028": "Agriculture intensity",
        "EA030": "Settlement pattern",
        "EA033": "Political hierarchy",
    }
    friendly_labels = {
        "EA028": {
            1: "No agriculture",
            2: "Casual",
            3: "Extensive or shifting",
            4: "Horticulture",
            5: "Intensive",
            6: "Intensive irrigated",
        },
        "EA030": {
            1: "Nomadic",
            2: "Semi-nomadic",
            3: "Semi-sedentary",
            4: "Impermanent villages",
            5: "Dispersed homesteads",
            6: "Hamlets",
            7: "Villages or towns",
            8: "Complex permanent",
        },
        "EA033": {
            1: "No hierarchy",
            2: "One level",
            3: "Two levels",
            4: "Three levels",
            5: "Four+ levels",
        },
        "EA042": {
            1: "Gathering",
            2: "Fishing",
            3: "Hunting",
            4: "Pastoralism",
            5: "Casual agriculture",
            6: "Extensive agriculture",
            7: "Intensive agriculture",
            8: "Mixed equal",
            9: "Agriculture unknown",
        },
        "EA043": {
            1: "Patrilineal",
            2: "Duolateral",
            3: "Matrilineal",
            4: "Quasi-lineages",
            5: "Ambilineal",
            6: "Bilateral",
            7: "Mixed",
        },
        "EA070": {
            1: "No slavery",
            2: "Nonhereditary",
            3: "Slavery (unknown heredity)",
            4: "Hereditary",
        },
        "EA009": {
            1: "Monogamous",
            2: "Limited polygyny",
            3: "Polygyny, sororal cohabit",
            4: "Polygyny, sororal separate",
            5: "Polygyny, non-sororal separate",
            6: "Polygyny, non-sororal cohabit",
            7: "Polyandrous",
        },
        "EA012": {
            1: "Avunculocal",
            2: "Ambilocal",
            3: "Avuncu-uxorilocal",
            4: "Avuncu-virilocal",
            5: "Matrilocal",
            6: "Neolocal",
            7: "Separate households",
            8: "Patrilocal",
            9: "Uxorilocal",
            10: "Virilocal",
            11: "Ambi-uxorilocal",
            12: "Ambi-virilocal",
        },
    }
    schema = {}
    for var in RF_INPUT_VARS:
        info = ALL_VARIABLES.get(var, {})
        if not info:
            continue
        if info["type"] == "categorical":
            labels = info.get("labels", {})
            if var in friendly_labels:
                labels = friendly_labels[var]
            schema[var] = {
                "type": "categorical",
                "valid_values": info.get("valid_values", []),
                "labels": labels,
                "name": friendly_names.get(var, info.get("name", var)),
            }
        else:
            schema[var] = {
                "type": info.get("type", "continuous"),
                "min": info.get("min", 0),
                "max": info.get("max", 1),
                "name": friendly_names.get(var, info.get("name", var)),
            }
    return render_template("index.html", schema_json=json.dumps(schema))


@app.route("/report", methods=["GET"])
def report():
    return render_template("report.html")


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
