import sqlite3

conn = sqlite3.connect("../database/mapped.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mapped_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    salt_strength TEXT UNIQUE,
    alt1 TEXT,
    alt2 TEXT,
    alt3 TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()