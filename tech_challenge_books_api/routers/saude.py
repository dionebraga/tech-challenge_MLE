from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from tech_challenge_books_api.infra.database import get_db

router = APIRouter(prefix="/api/v1", tags=["❤️ Saúde"])


@router.get(
    "/health",
    summary="Verificar Saúde da API ❤️",
    description="Verifica se a API está de pé e se o banco responde.",
)
def health(db: Session = Depends(get_db)):
    ok_db = False
    try:
        db.execute(text("SELECT 1"))
        ok_db = True
    except Exception:
        ok_db = False
    return {"status": "ok", "database": ok_db}
