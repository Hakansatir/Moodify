from __future__ import annotations
from pathlib import Path
import pickle


def load_model(path: Path):
    with open(path, "rb") as f:
        return pickle.load(f)
