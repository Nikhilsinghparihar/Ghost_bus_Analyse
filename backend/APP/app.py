import sqlite3

def init_db():
    conn = sqlite3.connect("voting.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        mobile TEXT,
        aadhaar TEXT UNIQUE,
        city TEXT,
        state TEXT
    )
    """)

    # Votes table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS votes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aadhaar TEXT,
        party TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()