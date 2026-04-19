from fastapi import APIRouter, HTTPException, status
from datetime import date
from typing import List
from schemas import NoteCreate, NoteUpdate, NoteResponse
from storage import notes_db, next_id

router = APIRouter(
    prefix="/notes",
    tags=["Notes"],
)

@router.post("/", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate):
    note_id = next_id()

    new_note = {
        "id": note_id,
        "title": note.title,
        "content": note.content,
        "created_at": date.today().isoformat(),
    }

    notes_db[note_id] = new_note
    return new_note

@router.get("/", response_model=List[NoteResponse])
def get_all_notes():
    return list(notes_db.values())

@router.get("/", response_model=NoteResponse)
def get_one_note(note_id: int):
    note = notes_db.get(note_id)

    if not note:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f"Note with Id {note_id} not found"
        )

    return note

@router.put("/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, data: NoteUpdate):
    note = notes_db.get(note_id)
    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found",
        )
    
    if data.title is not None:
        note["title"] = data.title

    if data.content is not None:
        note["content"] = data.content
 
    notes_db[note_id] = note
    return note


@router.delete("/{note_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int):
    note = notes_db.pop(note_id, None)
    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found",
        )
