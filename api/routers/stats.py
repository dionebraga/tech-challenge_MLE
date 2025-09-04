from fastapi import APIRouter
from ..deps import get_conn

router = APIRouter(prefix="/api/v1", tags=["stats"])

@router.get("/health")
def health():
    with get_conn() as con:
        n = con.execute("SELECT COUNT(*) AS n FROM books").fetchone()["n"]
    return {"status": "ok", "total_books": n}

@router.get("/stats/overview")
def stats_overview():
    with get_conn() as con:
        row = con.execute("SELECT COUNT(*) AS total_books, AVG(price) AS avg_price FROM books").fetchone()
        dist = con.execute("SELECT rating, COUNT(*) as qty FROM books GROUP BY rating").fetchall()
    return {"total_books": row["total_books"], "avg_price": row["avg_price"],
            "rating_distribution": {r["rating"]: r["qty"] for r in dist}}

