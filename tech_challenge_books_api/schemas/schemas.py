from pydantic import BaseModel
from typing import Optional

# 📚 Livros
class BookBase(BaseModel):
    title: str
    price: float
    stock: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str]
    price: Optional[float]
    stock: Optional[int]

class Book(BookBase):
    id: int
    class Config:
        orm_mode = True

# 🏷️ Categorias
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str]

class Category(CategoryBase):
    id: int
    class Config:
        orm_mode = True
