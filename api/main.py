from fastapi import FastAPI
from .routers import books, categories, stats

app = FastAPI(title="Books API", version="1.0.0")

app.include_router(books.router)
app.include_router(categories.router)
app.include_router(stats.router)

