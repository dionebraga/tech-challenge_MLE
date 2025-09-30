from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from tech_challenge_books_api.infra.database import get_db
from models.category_model import Categoria
from tech_challenge_books_api.schemas.categoria_schema import CategoriaOut, CategoriaCreate

router = APIRouter(prefix="/api/v1", tags=["🏷️ Categorias"])

# GET /api/v1/categorias - Lista todas as categorias
@router.get(
    "/categorias",
    response_model=List[CategoriaOut],
    summary="Buscar Categorias 🏷️",
    description="Retorna a lista de categorias de livros disponíveis na base.",
)
def listar_categorias(db: Session = Depends(get_db)):
    return db.query(Categoria).all()


# POST /api/v1/categorias - Criar categoria
@router.post(
    "/categorias",
    response_model=CategoriaOut,
    summary="Criar Categoria ✍️",
    description="Adiciona uma nova categoria à base de dados.",
)
def criar_categoria(dados: CategoriaCreate, db: Session = Depends(get_db)):
    categoria = Categoria(**dados.dict())
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria
