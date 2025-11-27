import os
import subprocess

from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.models.chat_request import ChatRequest
from src.models.message import Message
from src.services.rag_service import get_rag_response

app = FastAPI()

# Placeholder for API router
api_router = APIRouter()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow the Frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all types (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@api_router.get("/health")
async def health_check():
    return {"status": "ok"}


@api_router.post("/chat", response_model=Message)
async def chat(request: ChatRequest):
    response_content = get_rag_response(request.query, request.query)
    return Message(role="assistant", content=response_content)


@api_router.post("/index")
async def index_content():
    try:
        # Execute the indexing script
        subprocess.run(["python", "scripts/index_book.py"], check=True)
        return {"status": "Indexing started successfully"}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Indexing failed: {e}")


app.include_router(api_router, prefix="/api")
