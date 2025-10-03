from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from tech_challenge_books_api.routers import livros, categorias, saude, scraping, relatorios
from tech_challenge_books_api.infra.database import Base, engine
from tech_challenge_books_api.models import livro_model, categoria_model

# 🔹 Cria todas as tabelas no banco automaticamente
Base.metadata.create_all(bind=engine)

# 🚀 Instância principal
app = FastAPI(
    title="📚 Tech Challenge — API de Livros",
    version="1.0",
    description="API pública para consulta e gerenciamento de livros extraídos via Web Scraping.",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# 🔗 Inclui as rotas
app.include_router(livros.router)
app.include_router(categorias.router)
app.include_router(saude.router)
app.include_router(scraping.router)
app.include_router(relatorios.router)

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
        {"name": "🏷️ Categorias", "description": "Gerenciar categorias de livros"},
        {
            "name": "📊 Estatísticas",
            "description": "Relatórios e métricas (gráficos interativos e estáticos).",
            "externalDocs": {
                "description": "📈 Abrir Dashboard interativo",
                "url": "/api/v1/relatorios/dashboard"
            },
        },
        {"name": "🕷️ Scraping", "description": "Executar scraping de livros online"},
        {"name": "❤️ Saúde", "description": "Verificação de status da API"},
    ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# 🏠 Rota raiz
@app.get("/", tags=["❤️ Saúde"], summary="Página inicial 🏠", include_in_schema=False)
def root():
    return {"mensagem": "Bem-vindo(a) à API de Livros do Tech Challenge, com Dione Braga!"}