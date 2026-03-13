from fastapi import APIRouter
from typing import List, Dict
from db import cursor, conn
import json

router = APIRouter()

@router.post("/save")
def save_mapping(items: List[Dict]):

    for item in items:

        salt_strength = item.get("Salt + Strength")
        dosage_form = item.get("Dosage Form")

        alternatives = [
            value
            for key, value in item.items()
            if key.startswith("Alt ") and value
        ]

        cursor.execute(
            """
            INSERT INTO mapped_products (salt_strength, dosage_form, alternatives)
            VALUES (%s, %s, %s)
            ON CONFLICT (salt_strength, dosage_form)
            DO UPDATE SET
                alternatives = EXCLUDED.alternatives,
                updated_at = CURRENT_TIMESTAMP
            """,
            (salt_strength, dosage_form, json.dumps(alternatives)),
        )

    conn.commit()

    return {"status": "saved"}