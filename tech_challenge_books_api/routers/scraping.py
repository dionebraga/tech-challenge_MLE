from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..infra.database import get_db
from ..scripts.scraping import scrape_books

router = APIRouter(prefix="/api/v1/scraping", tags=["🕷️ Scraping"])

# 🚀 Executar scraping e salvar CSV
@router.post("/trigger", summary="Rodar scraping e salvar no banco")
def executar_scraping(db: Session = Depends(get_db)):
    try:
        result = scrape_books("books.csv", max_pages=2)
        return {"status": "ok", "mensagem": "Scraping executado com sucesso!", "detalhes": result}
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}
