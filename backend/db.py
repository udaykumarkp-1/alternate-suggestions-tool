import psycopg2

DATABASE_URL = "postgresql://postgres.bqeyuzmfajnnlidwycsm:UdayKumarKP2003@aws-1-ap-south-1.pooler.supabase.com:5432/postgres"

conn = None
cursor = None

try:
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
    cursor = conn.cursor()

    print("✅ Connected to Supabase PostgreSQL database")

except Exception as e:
    print("❌ Database connection failed:", e)


create_table_query = """
CREATE TABLE IF NOT EXISTS mapped_products (
    id SERIAL PRIMARY KEY,
    salt_strength TEXT,
    dosage_form TEXT,
    alternatives TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

if cursor:
    cursor.execute(create_table_query)