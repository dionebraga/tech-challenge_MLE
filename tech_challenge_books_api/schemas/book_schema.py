from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    category_id: int

class BookCreate(BookBase):
    """📘 Schema para criação de livro"""
    pass

class BookUpdate(BookBase):
    """✏️ Schema para atualização de livro"""
    pass

class Book(BookBase):
    """📚 Schema de resposta (livro completo)"""
    id: int

    class Config:
        from_attributes = True
