from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Title of the note")
    content: str = Field(..., min_length=1, max_length=200, description= "Content of the note")


class NoteUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = Field(None, min_length=1, max_length=200)


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: date