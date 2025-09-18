from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func

from tech_challenge_books_api.infra.database import get_db
from tech_challenge_books_api.models.livro_model import Livro
from tech_challenge_books_api.models.categoria_model import Categoria
from tech_challenge_books_api.schemas.livro_schema import LivroOut, LivroCreate, LivroUpdate

router = APIRouter(prefix="/api/v1", tags=["📘 Livros"])

# GET /api/v1/livros - Lista todos os livros
@router.get(
    "/livros",
    response_model=List[LivroOut],
    summary="Buscar Livros 📚",
    description="Retorna a lista completa de livros disponíveis na base.",
)
def listar_livros(db: Session = Depends(get_db)):
    return db.query(Livro).all()


# GET /api/v1/livros/{id} - Detalhar um livro
@router.get(
    "/livros/{id}",
    response_model=LivroOut,
    summary="Detalhar Livro 🔍",
    description="Busca um livro específico pelo seu ID.",
)
def buscar_livro(id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado ❌")
    return livro


# POST /api/v1/livros - Criar novo livro
@router.post(
    "/livros",
    response_model=LivroOut,
    summary="Criar Livro ✍️",
    description="Adiciona um novo livro à base de dados.",
)
def criar_livro(dados: LivroCreate, db: Session = Depends(get_db)):
    livro = Livro(**dados.dict())
    db.add(livro)
    db.commit()
    db.refresh(livro)
    return livro


# PUT /api/v1/livros/{id} - Atualizar livro
@router.put(
    "/livros/{id}",
    response_model=LivroOut,
    summary="Atualizar Livro 🔄",
    description="Atualiza todos os dados de um livro existente.",
)
def atualizar_livro(id: int, dados: LivroUpdate, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado ❌")

    for key, value in dados.dict(exclude_unset=True).items():
        setattr(livro, key, value)

    db.commit()
    db.refresh(livro)
    return livro


# DELETE /api/v1/livros/{id} - Deletar livro
@router.delete(
    "/livros/{id}",
    summary="Deletar Livro 🗑️",
    description="Remove um livro da base de dados.",
)
def deletar_livro(id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado ❌")

    db.delete(livro)
    db.commit()
    return {"message": "Livro deletado com sucesso ✅"}
