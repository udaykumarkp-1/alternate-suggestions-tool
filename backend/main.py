from fastapi import FastAPI
from pydantic import BaseModel
from db import cursor, conn

app = FastAPI()

class Mapping(BaseModel):
    salt_strength: str
    alt1: str
    alt2: str
    alt3: str

@app.post("/save")
def save_mapping(items: list[Mapping]):

    for i in items:
        cursor.execute("""
        INSERT INTO mapped_products (salt_strength, alt1, alt2, alt3)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(salt_strength)
        DO UPDATE SET
            alt1=excluded.alt1,
            alt2=excluded.alt2,
            alt3=excluded.alt3
        """, (i.salt_strength, i.alt1, i.alt2, i.alt3))

    conn.commit()
    return {"status": "saved"}

@app.get("/search")
def search(q: str):

    q = q.strip()   # remove whitespace from query

    rows = cursor.execute("""
    SELECT DISTINCT salt_strength, alt1, alt2, alt3
    FROM mapped_products
    WHERE TRIM(salt_strength) LIKE ?
       OR TRIM(alt1) LIKE ?
       OR TRIM(alt2) LIKE ?
       OR TRIM(alt3) LIKE ?
    """, (f"%{q}%",)*4).fetchall()

    return rows


# 🔥 ADD THIS
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)