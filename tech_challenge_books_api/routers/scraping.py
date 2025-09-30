from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from tech_challenge_books_api.infra.database import get_db
from tech_challenge_books_api.models.book_model import Livro
from tech_challenge_books_api.models.category_model import Categoria
from tech_challenge_books_api.scripts.scraping import scrape_books
import csv

router = APIRouter(prefix="/api/v1/scraping", tags=["🕷️ Scraping"])

@router.post("/trigger", summary="Rodar scraping e salvar no banco")
def trigger_scraping(db: Session = Depends(get_db)):
    """
    Executa o scraping do site books.toscrape.com,
    salva os dados em CSV e popula o banco automaticamente.
    """
    total = scrape_books("books.csv", max_pages=3)

    with open("books.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            categoria = db.query(Categoria).filter_by(nome="Geral").first()
            if not categoria:
                categoria = Categoria(nome="Geral")
                db.add(categoria)
                db.commit()
                db.refresh(categoria)

            livro = Livro(
                titulo=row["title"],
                descricao=f"Livro extraído com rating {row['rating']}",
                preco=float(row["price"]),
                categoria_id=categoria.id
            )
            db.add(livro)
        db.commit()

    return {"message": f"✅ {total} livros extraídos e salvos no banco!"}
