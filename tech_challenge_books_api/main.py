from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from .routers import livros, categorias, saude, scraping

app = FastAPI(
    title="📚 Tech Challenge — API de Livros",
    version="1.0.0",
    description="API pública para consulta de livros extraídos via Web Scraping.",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# 🔗 Inclui as rotas
app.include_router(livros.router)
app.include_router(categorias.router)
app.include_router(saude.router)
app.include_router(scraping.router)

# 🔖 Customização Swagger
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
        {"name": "📘 Livros", "description": "CRUD de livros"},
        {"name": "🏷️ Categorias", "description": "Gerenciar categorias"},
        {"name": "📊 Estatísticas", "description": "Relatórios e métricas"},
        {"name": "❤️ Saúde", "description": "Status da API"},
        {"name": "🕷️ Scraping", "description": "Executar scraping de livros"},
    ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.get("/", tags=["❤️ Saúde"], summary="Página inicial 🏠", include_in_schema=False)
def root():
    return {"mensagem": "Bem-vindo(a) à API de Livros do Tech Challenge!"}
