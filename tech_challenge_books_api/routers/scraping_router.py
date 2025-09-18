from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from tech_challenge_books_api.infra.database import get_db
from tech_challenge_books_api.scripts.scraping_books import scrape_books

router = APIRouter(prefix="/api/v1/scraping", tags=["📚 Scraping"])

@router.post("/trigger", summary="Iniciar Scraping de Livros")
def trigger_scraping(db: Session = Depends(get_db)):
    """
    Executa o scraping no site Books to Scrape e salva os livros no banco de dados.
    """
    result = scrape_books(db)
    return result
