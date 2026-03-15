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
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (salt_strength, dosage_form)
);
"""

# ✅ FIX: Also add UNIQUE constraint to existing table if it was already created without it
add_constraint_query = """
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'mapped_products_salt_strength_dosage_form_key'
    ) THEN
        ALTER TABLE mapped_products
        ADD CONSTRAINT mapped_products_salt_strength_dosage_form_key
        UNIQUE (salt_strength, dosage_form);
    END IF;
END$$;
"""

if cursor:
    cursor.execute(create_table_query)
    try:
        cursor.execute(add_constraint_query)
        print("✅ UNIQUE constraint ensured on (salt_strength, dosage_form)")
    except Exception as e:
        print("Constraint note:", e)