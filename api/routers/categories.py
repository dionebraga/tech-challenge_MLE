from fastapi import APIRouter
from ..deps import get_conn

router = APIRouter(prefix="/api/v1", tags=["categories"])

@router.get("/categories")
def list_categories():
    with get_conn() as con:
        rows = con.execute("SELECT DISTINCT category FROM books ORDER BY category").fetchall()
    return [r["category"] for r in rows]

