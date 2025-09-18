from pydantic import BaseModel
from typing import Optional

# Schema de saída para Livro 📚
class LivroOut(BaseModel):
    id: int
    titulo: str
    descricao: str
    preco: float
    categoria_id: Optional[int]

    class Config:
        orm_mode = True


# Schema de criação de Livro ✍️
class LivroCreate(BaseModel):
    titulo: str
    descricao: str
    preco: float
    categoria_id: Optional[int]


# Schema de atualização de Livro 🔄
class LivroUpdate(BaseModel):
    titulo: Optional[str]
    descricao: Optional[str]
    preco: Optional[float]
    categoria_id: Optional[int]
