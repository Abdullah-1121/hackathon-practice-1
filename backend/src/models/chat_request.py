from pydantic import BaseModel
from typing import List, Optional
from backend.src.models.message import Message

class ChatRequest(BaseModel):
    messages: List[Message]
    selected_text: Optional[str] = None
