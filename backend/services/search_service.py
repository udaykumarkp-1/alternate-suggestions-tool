from db import cursor
import json


def search_products(query):

    cursor.execute(
        """
        SELECT salt_strength, dosage_form, alternatives
        FROM mapped_products
        WHERE salt_strength ILIKE %s
        OR alternatives ILIKE %s
        """,
        (f"%{query}%", f"%{query}%")
    )

    rows = cursor.fetchall()

    results = []

    for salt, dosage, alt_json in rows:

        alternatives = json.loads(alt_json)

        row = {
            "Salt + Strength": salt,
            "Dosage Form": dosage
        }

        # expand alternatives into columns
        for i, alt in enumerate(alternatives):
            row[f"Alt {i+1}"] = alt

        results.append(row)

    return results