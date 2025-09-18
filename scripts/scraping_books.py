import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from tech_challenge_books_api.models.livro_model import Livro
from tech_challenge_books_api.models.categoria_model import Categoria

BASE_URL = "https://books.toscrape.com/"

def scrape_books(db: Session):
    url = BASE_URL + "catalogue/page-1.html"
    all_books = []

    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")
        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.replace("£", "").strip()
            rating = book.p["class"][1] if len(book.p["class"]) > 1 else "Unrated"
            availability = book.find("p", class_="instock availability").text.strip()
            category = "Unknown"  # simplificado (poderia buscar pela URL da categoria)
            image = BASE_URL + book.find("img")["src"].replace("../../", "")

            # Salvar categoria ou recuperar existente
            db_category = db.query(Categoria).filter_by(nome=category).first()
            if not db_category:
                db_category = Categoria(nome=category)
                db.add(db_category)
                db.commit()
                db.refresh(db_category)

            # Criar livro
            new_book = Livro(
                titulo=title,
                descricao=f"Livro {title} da categoria {category}",
                preco=float(price),
                avaliacao=rating,
                disponibilidade=availability,
                imagem=image,
                categoria_id=db_category.id
            )
            db.add(new_book)

        db.commit()

        # Próxima página
        next_page = soup.find("li", class_="next")
        if next_page:
            url = BASE_URL + "catalogue/" + next_page.a["href"]
        else:
            url = None

    return {"message": "Scraping concluído e dados salvos no banco!"}
