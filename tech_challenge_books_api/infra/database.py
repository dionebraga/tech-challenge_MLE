from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 🔹 Caminho do banco (aqui usando SQLite local, pode trocar se quiser outro banco)
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# 🔹 Cria o engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 🔹 Cria a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🔹 Base para os modelos
Base = declarative_base()

# 🔹 Função para usar no FastAPI (injeção de dependência)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from .database import Base, engine
from tech_challenge_books_api.models import livro_model, categoria_model

def init_db():
    """Cria as tabelas no banco de dados"""
    Base.metadata.create_all(bind=engine)
# Importa os modelos para registrar as tabelas