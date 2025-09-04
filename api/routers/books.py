from fastapi import APIRouter, HTTPException, Query
from ..deps import get_conn

router = APIRouter(prefix="/api/v1", tags=["books"])

@router.get("/books")
def list_books(limit: int = Query(100, ge=1, le=500), offset: int = 0):
    with get_conn() as con:
        rows = con.execute("SELECT * FROM books LIMIT ? OFFSET ?", (limit, offset)).fetchall()
    return [dict(r) for r in rows]

@router.get("/books/{book_id}")
def get_book(book_id: int):
    with get_conn() as con:
        r = con.execute("SELECT * FROM books WHERE id=?", (book_id,)).fetchone()
    if not r:
        raise HTTPException(status_code=404, detail="Book not found")
    return dict(r)

@router.get("/books/search")
def search_books(title: str | None = None, category: str | None = None):
    q = "SELECT * FROM books WHERE 1=1"
    params = []
    if title:
        q += " AND LOWER(title) LIKE ?"; params.append(f"%{title.lower()}%")
    if category:
        q += " AND LOWER(category)=?"; params.append(category.lower())
    with get_conn() as con:
        rows = con.execute(q, tuple(params)).fetchall()
    return [dict(r) for r in rows]
