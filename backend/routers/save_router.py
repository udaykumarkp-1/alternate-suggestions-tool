from fastapi import APIRouter
from typing import List, Dict
from backend.db import cursor, conn
import json

router = APIRouter()

@router.post("/save")
def save_mapping(items: List[Dict]):

    for item in items:

        salt_strength = item.get("Salt + Strength")

        alternatives = [
            value
            for key, value in item.items()
            if key.startswith("Alt ") and value
        ]

        cursor.execute(
            """
            INSERT OR REPLACE INTO mapped_products
            (salt_strength, alternatives)
            VALUES (?, ?)
            """,
            (salt_strength, json.dumps(alternatives)),
        )

    conn.commit()

    return {"status": "saved"}