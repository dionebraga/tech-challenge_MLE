from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL do banco de dados (aqui SQLite, pode trocar se usar outro)
SQLALCHEMY_DATABASE_URL = "sqlite:///./livros.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Função de dependência para usar nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar as tabelas
def create_db():
    Base.metadata.create_all(bind=engine)
    print("Banco de dados e tabelas criados com sucesso! ✅")