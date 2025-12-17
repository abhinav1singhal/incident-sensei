from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
import os

from app.config import settings
from app.routers import webhook, incidents
from app.services.kafka_service import kafka_service

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    kafka_service.start()
    yield
    # Shutdown
    kafka_service.stop()

app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

# Create static dir if not exists
os.makedirs("app/static/audio", exist_ok=True)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(webhook.router)
app.include_router(incidents.router)

# CORS Configuration
origins = [
    "http://localhost:5173",  # Vite default
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
