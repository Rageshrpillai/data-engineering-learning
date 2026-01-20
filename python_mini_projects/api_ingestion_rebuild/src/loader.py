from db import get_db_connection
from datetime import datetime,timezone
import logging

def load_to_postgres(users):
    conn = get_db_connection()
    cursor = conn.cursor()

    upsert_sql="""
     INSERT INTO users (id, name , email , updated_at)
     VALUES (%s,%s,%s,%s)
     ON CONFLICT (id)
     DO UPDATE SET
        name = EXCLUDED.name,
        email = EXCLUDED.email,
        updated_at= EXCLUDED.updated_at;
    """

    try:
        logging.info("Users data insertion Started")
        now = datetime.now(timezone.utc)
        for user in users:
            cursor.execute(upsert_sql, (
            user["id"],
            user.get("name"),
            user["email"],
            now
        ))
        conn.commit()
        logging.info("Users data loaded successfully")    

    except Exception:
        conn.rollback()
        logging.exception("pipeline failed during upsert method")
        raise
    finally:
        cursor.close()
        conn.close()
