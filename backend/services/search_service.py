from backend.db import cursor
import json


def search_products(q: str):

    q = q.strip()

    rows = cursor.execute(
        """
        SELECT salt_strength, alternatives
        FROM mapped_products
        WHERE salt_strength LIKE ?
        OR alternatives LIKE ?
        """,
        (f"%{q}%", f"%{q}%"),
    ).fetchall()

    results = []

    for salt_strength, alternatives_json in rows:

        alternatives = json.loads(alternatives_json)

        row = {"Salt + Strength": salt_strength}

        for i, alt in enumerate(alternatives):
            row[f"Alt {i+1}"] = alt

        results.append(row)

    return results