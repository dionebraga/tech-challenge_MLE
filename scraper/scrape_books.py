import csv, time, requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd, sqlite3

BASE = "https://books.toscrape.com/"
CSV_OUT = "data/books.csv"
DB_OUT = "data/books.db"

def parse_book(card, category):
    title = card.h3.a["title"]
    price = card.select_one(".price_color").text.replace("£","").strip()
    rating = card.select_one(".star-rating")["class"][1]
    availability = card.select_one(".availability").text.strip()
    rel = card.h3.a["href"]
    detail_url = urljoin(BASE+"catalogue/", rel.replace("../../", ""))
    img_rel = card.select_one("img")["src"]
    image_url = urljoin(BASE, img_rel)
    return dict(title=title, price=float(price), rating=rating,
                availability=availability, category=category,
                image_url=image_url, detail_url=detail_url)

def scrape_category(cat_url, category):
    items = []
    url = cat_url
    while True:
        soup = BeautifulSoup(requests.get(url, timeout=30).text, "lxml")
        for card in soup.select(".product_pod"):
            items.append(parse_book(card, category))
        nextp = soup.select_one(".next a")
        if not nextp: break
        url = urljoin(url, nextp["href"])
        time.sleep(0.2)
    return items

def main():
    soup = BeautifulSoup(requests.get(BASE, timeout=30).text, "lxml")
    cats = []
    for a in soup.select(".side_categories a"):
        href = a.get("href")
        name = a.text.strip()
        if "category/books/" in href and name.lower()!="books":
            cats.append((urljoin(BASE, href), name))

    rows = []
    for cat_url, name in cats:
        rows += scrape_category(cat_url, name)

    # salva CSV
    with open(CSV_OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)
    print(f"✅ CSV salvo com {len(rows)} livros")

    # salva SQLite
    df = pd.DataFrame(rows)
    con = sqlite3.connect(DB_OUT)
    df.to_sql("books", con, if_exists="replace", index_label="id")
    con.close()
    print(f"✅ Banco SQLite salvo em {DB_OUT}")

if __name__ == "__main__":
    main()
