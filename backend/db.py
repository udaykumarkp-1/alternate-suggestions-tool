import sqlite3

# Connect database
conn = sqlite3.connect("mapped_v2.db", check_same_thread=False)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS mapped_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    salt_strength TEXT UNIQUE,
    alternatives TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()