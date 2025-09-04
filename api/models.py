from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    price: float
    rating: str
    availability: str
    category: str
    image_url: str
    detail_url: str

class Health(BaseModel):
    status: str
    total_books: int
