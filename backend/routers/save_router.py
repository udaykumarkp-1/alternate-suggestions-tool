from fastapi import APIRouter
from typing import List, Dict
from db import cursor, conn
import json

router = APIRouter()

@router.post("/save")
def save_mapping(items: List[Dict]):

    saved = 0
    skipped = 0
    errors = 0

    for item in items:

        salt_strength = item.get("Salt + Strength")
        dosage_form = item.get("Dosage Form")

        # ✅ FIX: Skip rows where salt or dosage is missing
        if not salt_strength or not dosage_form:
            skipped += 1
            continue

        salt_strength = str(salt_strength).strip()
        dosage_form = str(dosage_form).strip()

        # ✅ FIX: Skip if stripped values are empty
        if not salt_strength or not dosage_form:
            skipped += 1
            continue

        alternatives = [
            str(value).strip()
            for key, value in item.items()
            if key.startswith("Alt ") and value and str(value).strip()
        ]

        try:
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
            saved += 1

        except Exception as e:
            print(f"❌ Row error ({salt_strength}, {dosage_form}): {e}")
            errors += 1

    conn.commit()

    print(f"✅ Save complete: {saved} saved, {skipped} skipped, {errors} errors")

    return {"status": "saved", "saved": saved, "skipped": skipped, "errors": errors}