from pydantic import BaseModel
from typing import Optional, Any


class WebScrapSummarizerSchema(BaseModel):
    id: str
    url: str
    language: str


class SuccessResponse(BaseModel):
    data: Optional[Any] = None
    detail: Optional[Any] = None
