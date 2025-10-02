import csv
import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from tech_challenge_books_api.models.livro_model import Livro
from tech_challenge_books_api.models.categoria_model import Categoria
from tech_challenge_books_api.infra.database import SessionLocal

BASE_URL = "https://books.toscrape.com/"

def scrape_books(csv_path: str = "books.csv", max_pages: int = 3):
    """Extrai livros do site, insere no banco e salva também em CSV"""
    session: Session = SessionLocal()
    livros_extraidos = []

    try:
        page = 1
        while page <= max_pages:
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

                # 🔹 Corrige preço (remove £ e possíveis caracteres estranhos como Â)
                raw_price = book.find("p", class_="price_color").text
                price_str = raw_price.replace("£", "").replace("Â", "").strip()
                try:
                    price = float(price_str)
                except ValueError:
                    print(f"⚠️ Erro ao converter preço: {raw_price}")
                    price = 0.0

                rating = book.p["class"][1]  # Ex: "Three", "Five"
                availability = book.find("p", class_="instock availability").text.strip()

                # Detalhe para pegar categoria
                detail_url = BASE_URL + "catalogue/" + book.h3.a["href"]
                detail_resp = requests.get(detail_url)
                detail_soup = BeautifulSoup(detail_resp.text, "html.parser")
                category = detail_soup.find("ul", class_="breadcrumb").find_all("a")[2].text

                # Garante categoria no banco
                cat_obj = session.query(Categoria).filter_by(nome=category).first()
                if not cat_obj:
                    cat_obj = Categoria(nome=category)
                    session.add(cat_obj)
                    session.commit()

                # Adiciona livro no banco
                livro = Livro(
                    titulo=title,
                    descricao=f"Livro '{title}' da categoria {category}",
                    preco=price,
                    categoria_id=cat_obj.id,
                )
                session.add(livro)
                session.commit()

                # Guarda também para salvar em CSV
                livros_extraidos.append([title, price, rating, availability, category])

                # 🔹 Print debug no console
                print(f"📚 {title} | £{price} | {category}")

            page += 1

        # 🔹 Salva os livros em CSV
        with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Título", "Preço", "Avaliação", "Disponibilidade", "Categoria"])
            writer.writerows(livros_extraidos)

        print(f"✅ {len(livros_extraidos)} livros salvos em {csv_path}")
        return {"status": "ok", "total_livros": len(livros_extraidos), "csv": csv_path}

    except Exception as e:
        session.rollback()
        return {"status": "error", "message": str(e)}

    finally:
        session.close()
