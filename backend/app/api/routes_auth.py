from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode

from backend.app.core.config import SPOTIFY_CLIENT_ID, SPOTIFY_REDIRECT_URI, SPOTIFY_SCOPES
from backend.app.adapters.pkce import generate_code_challenge, generate_code_verifier
from backend.app.adapters.spotify_auth import exchange_code_for_token
from backend.app.adapters.token_store import save_tokens

router = APIRouter()

# DEV için basit: verifier'ı memory'de tutuyoruz.
# (Prod'da session/DB/Redis ile kullanıcı bazlı tutacağız.)
_PKCE_VERIFIER = None

@router.get("/login")
def login():
    global _PKCE_VERIFIER
    _PKCE_VERIFIER = generate_code_verifier()
    challenge = generate_code_challenge(_PKCE_VERIFIER)

    params = {
        "client_id": SPOTIFY_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": SPOTIFY_REDIRECT_URI,
        "code_challenge_method": "S256",
        "code_challenge": challenge,
        "scope": SPOTIFY_SCOPES,
    }

    url = "https://accounts.spotify.com/authorize?" + urlencode(params)
    return RedirectResponse(url)

@router.get("/callback")
async def callback(code: str):
    global _PKCE_VERIFIER
    tokens = await exchange_code_for_token(code=code, code_verifier=_PKCE_VERIFIER)
    save_tokens(tokens)
    return {"status": "ok", "message": "Spotify tokens saved. You can close this tab."}
