from fastapi import APIRouter
from db import cursor

router = APIRouter()

@router.get("/has_data")
def has_data():

    row = cursor.execute(
        "SELECT COUNT(*) FROM mapped_products"
    ).fetchone()

    return {"has_data": row[0] > 0}