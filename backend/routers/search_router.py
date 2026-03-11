from fastapi import APIRouter
from services.search_service import search_products
router = APIRouter()

@router.get("/search")
def search(q: str):
    return search_products(q)