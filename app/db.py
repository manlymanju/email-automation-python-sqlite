import sqlite3
import os

DB_NAME = "emails.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    base_dir = os.path.dirname(os.path.dirname(__file__))
    schema_path = os.path.join(base_dir, "sql", "schema.sql")

    with open(schema_path, "r") as f:
        schema = f.read()

    cursor.executescript(schema)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully.")



conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())
conn.close()
