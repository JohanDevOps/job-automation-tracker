import json
from pathlib import Path

DATA_PATH = Path("data/applications.json")

def load_applications():
    if DATA_PATH.exists():
        with open(DATA_PATH, "r") as f:
            return json.load(f)
    return []

def save_applications(apps):
    with open(DATA_PATH, "w") as f:
        json.dump(apps, f, indent=2)
