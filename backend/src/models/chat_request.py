from typing import List, Optional

from fastapi.params import Query
from pydantic import BaseModel

from src.models.message import Message


class ChatRequest(BaseModel):
    query: str
    selected_text: Optional[str] = None
