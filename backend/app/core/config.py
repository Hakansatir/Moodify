import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI", "")
SPOTIFY_SCOPES = os.getenv("SPOTIFY_SCOPES", "")

if not SPOTIFY_CLIENT_ID or not SPOTIFY_REDIRECT_URI:
    # dev ortamda kolay fark edilsin diye
    print("⚠️ Missing Spotify env vars: SPOTIFY_CLIENT_ID / SPOTIFY_REDIRECT_URI")
