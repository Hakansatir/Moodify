import httpx
from backend.app.core.config import SPOTIFY_CLIENT_ID, SPOTIFY_REDIRECT_URI

TOKEN_URL = "https://accounts.spotify.com/api/token"

async def exchange_code_for_token(code: str, code_verifier: str) -> dict:
    data = {
        "client_id": SPOTIFY_CLIENT_ID,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": SPOTIFY_REDIRECT_URI,
        "code_verifier": code_verifier,
    }
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.post(TOKEN_URL, data=data)
        r.raise_for_status()
        return r.json()
