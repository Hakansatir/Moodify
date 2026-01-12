from __future__ import annotations
from pathlib import Path
import json


def load_labels(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    # index → label sırasına çevir
    return [label for label, _ in sorted(data.items(), key=lambda x: x[1])]
