import psycopg2 
import logging

def get_db_connection():
    logging.info("Establishing database connection")
    conn=psycopg2.connect(
        host="localhost",
        database="python",
        user="postgres",
        password="1234"
    )
    return conn