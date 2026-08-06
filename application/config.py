from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AddonConfig:
    model_name: str
    model_front_template: str
    model_back_template: str

def load_addon_config() -> AddonConfig:
    config_path = Path(__file__).resolve().parents[1] / "config.json"

    with config_path.open(encoding="utf-8") as config_file:
        data = json.load(config_file)
    
    addon_config = AddonConfig(model_name=data["model_name"],
                               model_front_template=data["model_front_template"],
                               model_back_template=data["model_back_template"])

    return addon_config