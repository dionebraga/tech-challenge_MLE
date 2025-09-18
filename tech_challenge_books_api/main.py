from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

# 🚦 IMPORTES DOS ROUTERS
from tech_challenge_books_api.routers import livros, categorias, saude, scraping_router

app = FastAPI(
    title="📚 Tech Challenge — API de Livros",
    version="1.0.0",
    description=(
        "API pública para exploração de livros coletados via Web Scraping do site books.toscrape.com.\n\n"
        "Rotas em **PT-BR** (títulos/descrições) para facilitar a leitura no Swagger; "
        "URLs seguem o padrão exigido pelo desafio (em inglês).\n\n"
        "**Grupos de rotas:**\n"
        "- 📘 *Livros*\n"
        "- 🏷️ *Categorias*\n"
        "- 📊 *Estatísticas* (opcionais)\n"
        "- ❤️ *Saúde da API*\n"
        "- 🤖 *Scraping* (executar coleta de livros)\n"
    ),
    contact={
        "name": "Dione Braga",
        "url": "https://github.com/dionebraga/tech-challenge_MLE",
    },
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# Inclui os routers
app.include_router(livros.router)
app.include_router(categorias.router)
app.include_router(saude.router)
app.include_router(scraping_router.router)  # 👈 NOVO


# 🔖 Tags do Swagger com títulos em PT-BR + emojis
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    openapi_schema["tags"] = [
        {"name": "📘 Livros", "description": "Operações para listar, buscar e detalhar livros."},
        {"name": "🏷️ Categorias", "description": "Operações para listar categorias."},
        {"name": "📊 Estatísticas", "description": "Visão geral e análises (opcional)."},
        {"name": "❤️ Saúde", "description": "Status de saúde da API."},
        {"name": "🤖 Scraping", "description": "Executar coleta de livros do site Books to Scrape."},  # 👈 NOVO
    ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/", tags=["❤️ Saúde"], summary="Página inicial 🏠", include_in_schema=False)
def root():
    return {"message": "Bem-vindo(a) à API de Livros do Tech Challenge! Veja /docs para a documentação."}
