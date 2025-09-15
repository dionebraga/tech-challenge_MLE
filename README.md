# 📚 Tech Challenge - Books API  

API RESTful desenvolvida em **FastAPI** como parte do Tech Challenge, integrada com um **sistema de web scraping** que coleta dados de [Books to Scrape](https://books.toscrape.com/) e disponibiliza via endpoints documentados no **Swagger UI**.  

🚀 Deploy disponível em: [tech-challenge-mle.onrender.com](https://tech-challenge-mle.onrender.com/docs)  

---

## 🗂 Estrutura do Projeto

```bash
tech_challenge/
├── tech_challenge_books_api/
│   ├── main.py               # Ponto de entrada da aplicação
│   ├── infra/                # Configurações de banco e conexão
│   ├── routers/              # Rotas (books, categories)
│   ├── repositories/         # Lógica de persistência
│   ├── schemas/              # Schemas Pydantic (validação e responses)
│   └── models/               # Modelos ORM
├── scripts/                  # Scripts de scraping
│   └── scraping_books.py
├── data/                     # Dados exportados em CSV
├── requirements.txt          # Dependências do projeto
└── README.md
---
## ⚙️ Instalação e Configuração

Clone o repositório:

git clone https://github.com/seu-usuario/tech_challenge.git
cd tech_challenge

## Crie um ambiente virtual:

python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

## Instale as dependências:
pip install -r requirements.txt

Rode localmente:
uvicorn tech_challenge_books_api.main:app --reload

Acesse em: http://127.0.0.1:8000/docs

---
🌐 Documentação da API

A documentação interativa está disponível via Swagger UI:
👉 /docs

📖 Endpoints principais
📚 Livros (/api/v1/books)

GET / → Lista todos os livros.
POST / → Adiciona um novo livro.
PATCH /{id} → Atualiza informações de um livro.
DELETE /{id} → Remove um livro.

🏷 Categorias (/api/v1/categories)

GET / → Lista todas as categorias.
POST / → Adiciona uma nova categoria.
PATCH /{id} → Atualiza informações de uma categoria.
DELETE /{id} → Remove uma categoria.

📊 Exemplo de Request/Response
Criar um livro

Request:

POST /api/v1/books
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "price": 120.00,
  "category_id": 1
}


Response:

{
  "id": 10,
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "price": 120.00,
  "category_id": 1
}

🕸 Sistema de Web Scraping

Fonte: Books to Scrape
Script: scripts/scraping_books.py
Saída: data/books.csv
Executar scraping:
python scripts/scraping_books.py

---
🏗 Arquitetura do Projeto
[ Books.toscrape ] → [ Scraper ] → [ CSV/Data ] → [ API FastAPI ] → [ Usuário Final / Cientista de Dados ]

Escalabilidade: Arquitetura modular preparada para banco SQL real.

Integração futura: Conexão com modelos de ML para análise de preços, recomendações e previsões de demanda.

---
👨‍💻 Tecnologias Utilizadas
Python 3.12
FastAPI
Uvicorn
SQLAlchemy
Pydantic v2
BeautifulSoup4

---
💡 Autor: Dione Braga
📌 Projeto desenvolvido para o Tech Challenge - Engenharia de Dados / Machine Learning
