from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    """🏷️ Schema para criação de categoria"""
    pass

class CategoryUpdate(CategoryBase):
    """✏️ Schema para atualização de categoria"""
    pass

class CategoryResponse(CategoryBase):
    """🏷️ Schema de resposta (categoria completa)"""
    id: int

    class Config:
        from_attributes = True
