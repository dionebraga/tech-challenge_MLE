from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..infra.database import get_db
from ..models.livro_model import Livro
from ..schemas.livro_schema import LivroOut, LivroCreate, LivroUpdate

router = APIRouter(prefix="/api/v1/livros", tags=["📘 Livros"])

# 📖 Buscar todos os livros
@router.get("/", response_model=List[LivroOut], summary="Buscar Livros 📚")
def listar_livros(db: Session = Depends(get_db)):
    return db.query(Livro).all()

# 🔎 Buscar livro por ID
@router.get("/{livro_id}", response_model=LivroOut, summary="Buscar Livro por ID 🔍")
def buscar_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro

# ➕ Criar livro
@router.post("/", response_model=LivroOut, summary="Criar Livro ➕")
def criar_livro(livro: LivroCreate, db: Session = Depends(get_db)):
    novo_livro = Livro(**livro.dict())
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    return novo_livro

# ✏️ Atualizar livro
@router.put("/{livro_id}", response_model=LivroOut, summary="Atualizar Livro ✏️")
def atualizar_livro(livro_id: int, dados: LivroUpdate, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    for key, value in dados.dict(exclude_unset=True).items():
        setattr(livro, key, value)

    db.commit()
    db.refresh(livro)
    return livro

# ❌ Deletar livro
@router.delete("/{livro_id}", summary="Deletar Livro ❌")
def deletar_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    db.delete(livro)
    db.commit()
    return {"mensagem": "Livro deletado com sucesso"}
