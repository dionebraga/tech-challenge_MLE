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
```

---

## ⚙️ Instalação e Configuração

1. Clone o repositório:  
   ```bash
   git clone https://github.com/seu-usuario/tech_challenge.git
   cd tech_challenge
   ```

2. Crie um ambiente virtual:  
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:  
   ```bash
   pip install -r requirements.txt
   ```

4. Rode localmente:  
   ```bash
   uvicorn tech_challenge_books_api.main:app --reload
   ```

Acesse em: **http://127.0.0.1:8000/docs**

---

## 🌐 Documentação da API

A documentação interativa está disponível via **Swagger UI**:  
👉 [/docs](https://tech-challenge-mle.onrender.com/docs)  

### 📖 Endpoints principais

#### 📚 Livros (`/api/v1/books`)
- `GET /` → Lista todos os livros.  
- `POST /` → Adiciona um novo livro.  
- `PATCH /{id}` → Atualiza informações de um livro.  
- `DELETE /{id}` → Remove um livro.  

#### 🏷 Categorias (`/api/v1/categories`)
- `GET /` → Lista todas as categorias.  
- `POST /` → Adiciona uma nova categoria.  
- `PATCH /{id}` → Atualiza informações de uma categoria.  
- `DELETE /{id}` → Remove uma categoria.  

---

## 📊 Exemplo de Request/Response

### Criar um livro
**Request:**
```json
POST /api/v1/books
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "price": 120.00,
  "category_id": 1
}
```

**Response:**
```json
{
  "id": 10,
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "price": 120.00,
  "category_id": 1
}
```

---

## 🕸 Sistema de Web Scraping

- Fonte: [Books to Scrape](https://books.toscrape.com/)  
- Script: `scripts/scraping_books.py`  
- Saída: `data/books.csv`  

Executar scraping:
```bash
python scripts/scraping_books.py
```

---

## 🏗 Arquitetura do Projeto

```
[ Books.toscrape ] → [ Scraper ] → [ CSV/Data ] → [ API FastAPI ] → [ Usuário Final / Cientista de Dados ]
```

- **Escalabilidade:** Arquitetura modular preparada para banco SQL real.  
- **Integração futura:** Conexão com modelos de ML para análise de preços, recomendações e previsões de demanda.  

---

## 👨‍💻 Tecnologias Utilizadas
- [Python 3.12](https://www.python.org/)  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [Uvicorn](https://www.uvicorn.org/)  
- [SQLAlchemy](https://www.sqlalchemy.org/)  
- [Pydantic v2](https://docs.pydantic.dev/)  
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)  

---

💡 **Autor:** Dione Braga  
📌 Projeto desenvolvido para o **Tech Challenge - Engenharia de Dados / Machine Learning**  
# 📚 Tech Challenge — API de Livros

API desenvolvida como parte do **Tech Challenge** da fase, integrando conhecimentos de **Engenharia de Dados, APIs RESTful e Machine Learning**.  

O projeto implementa um **pipeline de scraping → transformação → disponibilização via API pública** para que cientistas de dados e serviços de recomendação possam consumir os dados de livros com facilidade.

---

## 🚀 Arquitetura

```mermaid
flowchart LR
    A[🌐 books.toscrape.com] -->|Scraping| B[(CSV / Banco de Dados)]
    B -->|Disponibilização| C[⚡ FastAPI]
    C -->|Deploy| D[☁️ Render]
    D -->|Consumo| E[👩‍💻 Cientistas de Dados / Serviços ML]

# 📚 Tech Challenge — API de Livros

API desenvolvida como parte do **Tech Challenge** da fase, integrando conhecimentos de **Engenharia de Dados, APIs RESTful e Machine Learning**.  

O projeto implementa um **pipeline de scraping → transformação → disponibilização via API pública** para que cientistas de dados e serviços de recomendação possam consumir os dados de livros com facilidade.

---

## 🚀 Arquitetura

```mermaid
flowchart LR
    A[🌐 books.toscrape.com] -->|Scraping| B[(CSV / Banco de Dados)]
    B -->|Disponibilização| C[⚡ FastAPI]
    C -->|Deploy| D[☁️ Render]
    D -->|Consumo| E[👩‍💻 Cientistas de Dados / Serviços ML]
