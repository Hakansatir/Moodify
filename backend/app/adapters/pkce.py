import base64
import hashlib
import os

def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")

def generate_code_verifier() -> str:
    return _b64url(os.urandom(64))

def generate_code_challenge(verifier: str) -> str:
    digest = hashlib.sha256(verifier.encode("utf-8")).digest()
    return _b64url(digest)
