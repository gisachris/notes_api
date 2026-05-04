from fastapi import FastAPI
from routers import notes

app = FastAPI(
    title = "Notes MiniProject App",
    description = "fastAPI learning with a mini project",
    version = "1.0.0"
)

@app.get("/")
def root():
    return { "message": "Welcome to the Notes API"}

app.include_router(notes.router)