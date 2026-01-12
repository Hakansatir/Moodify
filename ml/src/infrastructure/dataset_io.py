from __future__ import annotations

from pathlib import Path
from typing import Any
import json
import numpy as np


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def save_txt_matrix(path: Path, arr: np.ndarray) -> None:
    ensure_dir(path.parent)
    np.savetxt(str(path), arr)


def save_json(path: Path, obj: Any) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
