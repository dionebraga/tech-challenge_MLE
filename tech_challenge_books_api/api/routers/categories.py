﻿from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_categories():
    return {"message": "🏷️ Lista de categorias"}
