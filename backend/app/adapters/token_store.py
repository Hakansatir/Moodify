from pathlib import Path
import json
from typing import Any, Optional

TOKENS_PATH = Path("backend") / "tokens.json"

def save_tokens(tokens: dict) -> None:
    TOKENS_PATH.write_text(json.dumps(tokens, indent=2), encoding="utf-8")

def load_tokens() -> Optional[dict]:
    if not TOKENS_PATH.exists():
        return None
    return json.loads(TOKENS_PATH.read_text(encoding="utf-8"))
