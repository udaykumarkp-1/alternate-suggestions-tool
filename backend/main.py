from fastapi import FastAPI
from pydantic import BaseModel
from db import cursor, conn
import json
from typing import List, Dict

app = FastAPI()


# ==============================
# SAVE ENDPOINT (DYNAMIC ALTS)
# ==============================

@app.post("/save")
def save_mapping(items: List[Dict]):

    print("🔥 Received payload:")
    print(items)

    for item in items:

        salt_strength = item.get("Salt + Strength")

        print("➡ Processing:", salt_strength)

        # Collect dynamic Alt columns
        alternatives = [
            value for key, value in item.items()
            if key.startswith("Alt ") and value
        ]

        print("   Alternatives found:", alternatives)

        cursor.execute("""
        INSERT OR REPLACE INTO mapped_products (salt_strength, alternatives)
        VALUES (?, ?)
        """, (salt_strength, json.dumps(alternatives)))

    conn.commit()

    # Check row count after insert
    row_count = cursor.execute("SELECT COUNT(*) FROM mapped_products").fetchone()[0]
    print("✅ Total rows in DB after save:", row_count)

    return {"status": "saved"}


# ==============================
# SEARCH ENDPOINT (DYNAMIC ALTS)
# ==============================

@app.get("/search")
def search(q: str):

    q = q.strip()

    rows = cursor.execute("""
    SELECT salt_strength, alternatives
    FROM mapped_products
    WHERE salt_strength LIKE ?
    """, (f"%{q}%",)).fetchall()

    results = []

    for salt_strength, alternatives_json in rows:

        alternatives = json.loads(alternatives_json)

        row = {"Salt + Strength": salt_strength}

        for i, alt in enumerate(alternatives):
            row[f"Alt {i+1}"] = alt

        results.append(row)

    return results


# ==============================
# CHECK DATA EXISTS
# ==============================

@app.get("/has_data")
def has_data():
    row = cursor.execute("SELECT COUNT(*) FROM mapped_products").fetchone()
    return {"has_data": row[0] > 0}


# ==============================
# LOCAL RUN
# ==============================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)