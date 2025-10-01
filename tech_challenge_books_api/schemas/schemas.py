from pydantic import BaseModel
from typing import Optional

# 📚 Livros
class LivroBase(BaseModel):
    title: str
    price: float
    stock: int

class LivroCreate(LivroBase):
    pass

class LivroUpdate(BaseModel):
    title: Optional[str]
    price: Optional[float]
    stock: Optional[int]

class Livro(LivroBase):
    id: int
    class Config:
        orm_mode = True

# 🏷️ Categorias
class CategoriaBase(BaseModel):
    name: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(BaseModel):
    name: Optional[str]

class Categoria(CategoriaBase):
    id: int
    class Config:
        orm_mode = True
