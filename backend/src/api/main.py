import os
from fastapi import FastAPI, APIRouter

app = FastAPI()

# Placeholder for API router
api_router = APIRouter()

@api_router.get("/health")
async def health_check():
    return {"status": "ok"}

app.include_router(api_router, prefix="/api")

