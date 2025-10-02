from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from tech_challenge_books_api.infra.database import Base

class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    preco = Column(Float)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    categoria = relationship("Categoria", backref="livros")