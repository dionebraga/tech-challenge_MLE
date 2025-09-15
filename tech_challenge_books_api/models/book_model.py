from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from tech_challenge_books_api.infra.database import Base

# Modelo ORM de Livro 📚
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))

    # Relacionamento com Categoria 🏷️
    category = relationship("Category", back_populates="books")
