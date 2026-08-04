from pydantic import BaseModel

from .VocabCard import VocabCard

class VocabResult(BaseModel):
    success: bool
    card: VocabCard | None = None
    error: str | None = None