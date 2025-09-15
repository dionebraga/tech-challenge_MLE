from fastapi import APIRouter
from typing import List
from tech_challenge_books_api.schemas import Book, BookCreate, BookUpdate

router = APIRouter()

fake_books_db = []

@router.get("/", response_model=List[Book])
async def get_books():
    return fake_books_db

@router.post("/", response_model=Book)
async def create_book(book: BookCreate):
    new_book = {"id": len(fake_books_db) + 1, **book.dict()}
    fake_books_db.append(new_book)
    return new_book

@router.patch("/{book_id}", response_model=Book)
async def update_book(book_id: int, book: BookUpdate):
    for b in fake_books_db:
        if b["id"] == book_id:
            b.update(book.dict())
            return b
    return {"error": "Livro não encontrado"}

@router.delete("/{book_id}")
async def delete_book(book_id: int):
    global fake_books_db
    fake_books_db = [b for b in fake_books_db if b["id"] != book_id]
    return {"message": f"📕 Livro {book_id} removido com sucesso"}
