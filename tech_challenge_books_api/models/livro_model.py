from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from tech_challenge_books_api.infra.database import Base

# Modelo ORM de Livro 📚
class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    # Relacionamento com Categoria 🏷️
    categoria = relationship("Categoria", back_populates="livros")