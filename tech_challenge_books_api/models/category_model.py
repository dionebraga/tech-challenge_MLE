from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from tech_challenge_books_api.infra.database import Base

# Modelo ORM de Categoria 🏷️
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    # Relacionamento com Livros 📚
    books = relationship("Book", back_populates="category")
