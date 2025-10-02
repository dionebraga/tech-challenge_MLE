from fastapi import APIRouter
from tech_challenge_books_api.scripts.scraping import scrape_books

router = APIRouter(
    prefix="/api/v1/scraping",
    tags=["Scraping"],
)

@router.post("/trigger", summary="Rodar scraping e salvar no banco")
def trigger_scraping():
    """
    Executa o scraping do site books.toscrape.com,
    insere os livros e categorias no banco e retorna um resumo.
    """
    return scrape_books("books.csv", max_pages=2)