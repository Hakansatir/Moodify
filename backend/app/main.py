from fastapi import FastAPI
from backend.app.api.routes_health import router as health_router

app = FastAPI(title="Moodify Backend")

app.include_router(health_router, prefix="/health", tags=["health"])
