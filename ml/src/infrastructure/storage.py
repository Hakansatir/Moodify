from __future__ import annotations

from pathlib import Path
from typing import Any

import pickle


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def save_pickle(obj: Any, path: Path) -> None:
    ensure_dir(path.parent)
    with open(path, "wb") as f:
        pickle.dump(obj, f)


def write_text(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    path.write_text(content, encoding="utf-8")
