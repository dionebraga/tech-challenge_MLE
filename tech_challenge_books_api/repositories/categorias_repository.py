from sqlalchemy.orm import Session
from models.categoria_model import Categoria
from schemas.categoria_schema import CategoriaCreate, CategoriaUpdate

# 📖 Buscar todas as categorias
def get_all_categorias(db: Session):
    return db.query(Categoria).all()

# 🔎 Buscar categoria por ID
def get_categoria_by_id(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

# ➕ Criar nova categoria
def create_categoria(db: Session, categoria: CategoriaCreate):
    nova_categoria = Categoria(**categoria.dict())
    db.add(nova_categoria)
    db.commit()
    db.refresh(nova_categoria)
    return nova_categoria

# 📝 Atualizar categoria
def update_categoria(db: Session, categoria_id: int, categoria: CategoriaUpdate):
    categoria_existente = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if not categoria_existente:
        return None
    for chave, valor in categoria.dict(exclude_unset=True).items():
        setattr(categoria_existente, chave, valor)
    db.commit()
    db.refresh(categoria_existente)
    return categoria_existente

# ❌ Deletar categoria
def delete_categoria(db: Session, categoria_id: int):
    categoria_existente = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if not categoria_existente:
        return None
    db.delete(categoria_existente)
    db.commit()
    return True
