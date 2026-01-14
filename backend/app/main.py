from fastapi import FastAPI
from backend.app.api.routes_health import router as health_router
from backend.app.api.routes_auth import router as auth_router

app = FastAPI(title="Moodify Backend")

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])