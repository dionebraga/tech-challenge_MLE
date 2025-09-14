from fastapi import FastAPI
from contextlib import asynccontextmanager
from tech_challenge_books_api.infra.database import create_db
from tech_challenge_books_api.api.routers import books, categories

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

app = FastAPI(
    title="Books API",
    description="API de livros raspados do site books.toscrape.com",
    version="1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/dionebraga.json",
    lifespan=lifespan,
)

@app.get("/")
async def root():
    return {"message": "🚀 API de Livros no ar! Acesse /docs para ver a documentação."}

app.include_router(books.router, prefix="/api/v1/books", tags=["📚 Livros"])
app.include_router(categories.router, prefix="/api/v1/categories", tags=["🏷️ Categorias"])
