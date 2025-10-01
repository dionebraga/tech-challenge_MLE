from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from tech_challenge_books_api.infra.database import Base

# 🏷️ Modelo de Categoria
class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)

    # 🔗 Relacionamento com Livro
    livros = relationship("Livro", back_populates="categoria")
