from fastapi import APIRouter
from typing import List
from tech_challenge_books_api.schemas import CategoryResponse, CategoryCreate, CategoryUpdate

router = APIRouter()

fake_categories_db = []

@router.get("/", response_model=List[CategoryResponse])
async def get_categories():
    return fake_categories_db

@router.post("/", response_model=CategoryResponse)
async def create_category(category: CategoryCreate):
    new_category = {"id": len(fake_categories_db) + 1, **category.dict()}
    fake_categories_db.append(new_category)
    return new_category

@router.patch("/{category_id}", response_model=CategoryResponse)
async def update_category(category_id: int, category: CategoryUpdate):
    for c in fake_categories_db:
        if c["id"] == category_id:
            c.update(category.dict())
            return c
    return {"error": "Categoria não encontrada"}

@router.delete("/{category_id}")
async def delete_category(category_id: int):
    global fake_categories_db
    fake_categories_db = [c for c in fake_categories_db if c["id"] != category_id]
    return {"message": f"🏷️ Categoria {category_id} removida com sucesso"}
