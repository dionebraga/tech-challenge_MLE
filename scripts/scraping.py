import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from models.book_model import Livro
from models.category_model import Categoria
from tech_challenge_books_api.infra.database import SessionLocal

BASE_URL = "https://books.toscrape.com/"

def scrape_books():
    """Extrai livros do site e insere no banco"""
    session: Session = SessionLocal()

    try:
        page = 1
        while True:
            url = f"{BASE_URL}catalogue/page-{page}.html"
            response = requests.get(url)
            if response.status_code != 200:
                break

            soup = BeautifulSoup(response.text, "html.parser")
            books = soup.find_all("article", class_="product_pod")

            if not books:
                break

            for book in books:
                title = book.h3.a["title"]
                price = float(book.find("p", class_="price_color").text.replace("£", "").strip())
                rating = book.p["class"][1]  # Ex: "Three", "Five"
                availability = book.find("p", class_="instock availability").text.strip()

                # categoria (precisamos buscar do link da página do livro)
                detail_url = BASE_URL + "catalogue/" + book.h3.a["href"]
                detail_resp = requests.get(detail_url)
                detail_soup = BeautifulSoup(detail_resp.text, "html.parser")
                category = detail_soup.find("ul", class_="breadcrumb").find_all("a")[2].text

                # garante categoria no banco
                cat_obj = session.query(Categoria).filter_by(nome=category).first()
                if not cat_obj:
                    cat_obj = Categoria(nome=category)
                    session.add(cat_obj)
                    session.commit()

                # adiciona livro
                livro = Livro(
                    titulo=title,
                    descricao=f"Livro '{title}' da categoria {category}",
                    preco=price,
                    categoria_id=cat_obj.id,
                )
                session.add(livro)

            session.commit()
            page += 1

        return {"status": "ok", "message": "Livros importados com sucesso!"}
    except Exception as e:
        session.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        session.close()
