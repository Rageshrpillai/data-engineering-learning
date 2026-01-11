import pandas as pd
import psycopg2
import logging

# ---------------- LOGGING CONFIG (FILE + CONSOLE) ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)

logging.info("Pipeline started")

try:
    # ---------------- READ SOURCE ----------------
    logging.info("Reading CSV file")
    df = pd.read_csv("data/crm_customers.csv")
    total_rows = len(df)
    logging.info(f"Rows read from CSV: {total_rows}")

    # ---------------- CONNECT TO DATABASE ----------------
    logging.info("Connecting to PostgreSQL")
    conn = psycopg2.connect(
        host="localhost",
        database="python",
        user="postgres",
        password="1234"
    )
    cursor = conn.cursor()
    logging.info("Database connection successful")

    # ---------------- CREATE TABLE ----------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS public.crm_customers (
            customer_id INT PRIMARY KEY,
            customer_name VARCHAR(100),
            email VARCHAR(100),
            country VARCHAR(50),
            last_updated DATE
        );
    """)
    logging.info("crm_customers table ensured")

    # ---------------- UPSERT QUERY ----------------
    upsert_query = """
    INSERT INTO public.crm_customers (
        customer_id,
        customer_name,
        email,
        country,
        last_updated
    )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (customer_id)
    DO UPDATE SET
        customer_name = EXCLUDED.customer_name,
        email = EXCLUDED.email,
        country = EXCLUDED.country,
        last_updated = EXCLUDED.last_updated
    WHERE EXCLUDED.last_updated > crm_customers.last_updated;
    """

    inserted = 0
    updated = 0
    ignored = 0

    for row in df.itertuples(index=False):
        # Check if record already exists
        cursor.execute(
            "SELECT last_updated FROM public.crm_customers WHERE customer_id = %s",
            (row.customer_id,)
        )
        existing = cursor.fetchone()

        # Perform UPSERT
        cursor.execute(upsert_query, tuple(row))

        # Classify result
        if cursor.rowcount == 0:
            ignored += 1
        else:
            if existing is None:
                inserted += 1
            else:
                updated += 1

    # ---------------- COMMIT ----------------
    conn.commit()

    # ---------------- LOG RESULTS ----------------
    logging.info(f"Total rows processed : {total_rows}")
    logging.info(f"Rows inserted        : {inserted}")
    logging.info(f"Rows updated         : {updated}")
    logging.info(f"Rows ignored         : {ignored}")
    logging.info("Transaction committed successfully")

except Exception:
    logging.error("Pipeline failed", exc_info=True)
    if 'conn' in locals():
        conn.rollback()
        logging.info("Transaction rolled back")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    logging.info("Database connection closed")

logging.info("Pipeline finished")
