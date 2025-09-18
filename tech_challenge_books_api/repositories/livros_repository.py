from sqlalchemy.orm import Session
from tech_challenge_books_api.models.livro_model import Livro
from tech_challenge_books_api.schemas.livro_schema import LivroCreate, LivroUpdate

# 📖 Buscar todos os livros
def get_all_livros(db: Session):
    return db.query(Livro).all()

# 🔎 Buscar livro por ID
def get_livro_by_id(db: Session, livro_id: int):
    return db.query(Livro).filter(Livro.id == livro_id).first()

# ➕ Criar novo livro
def create_livro(db: Session, livro: LivroCreate):
    novo_livro = Livro(**livro.dict())
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    return novo_livro

# 📝 Atualizar livro
def update_livro(db: Session, livro_id: int, livro: LivroUpdate):
    livro_existente = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro_existente:
        return None
    for chave, valor in livro.dict(exclude_unset=True).items():
        setattr(livro_existente, chave, valor)
    db.commit()
    db.refresh(livro_existente)
    return livro_existente

# ❌ Deletar livro
def delete_livro(db: Session, livro_id: int):
    livro_existente = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro_existente:
        return None
    db.delete(livro_existente)
    db.commit()
    return True
