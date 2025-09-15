from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# 🔗 URL do banco de dados (SQLite por padrão)
DATABASE_URL = "sqlite:///./books.db"

# 🚀 Engine e sessão
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os models
Base = declarative_base()


# Criar o banco de dados
def create_db():
    Base.metadata.create_all(bind=engine)


# Dependência para obter a sessão do banco
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
