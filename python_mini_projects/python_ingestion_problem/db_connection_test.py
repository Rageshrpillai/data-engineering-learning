import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="python",
    user="postgres",
    password="1234"
)

print("Database connection successful")

conn.close()
