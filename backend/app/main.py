# FastAPI uygulamasının başlangıç noktası
# app/main.py

from fastapi import FastAPI
from backend.app.routers import health, upload

app = FastAPI()

# Register routes
backend.app.include_router(health.router)
backend.app.include_router(upload.router)
