from pydantic import BaseModel

# Schema de saída para Categoria 🏷️
class CategoriaOut(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True


# Schema de criação de Categoria ✍️
class CategoriaCreate(BaseModel):
    nome: str
# Schema de atualização de Categoria 🔄
class CategoriaUpdate(BaseModel):
    nome: str | None = None
