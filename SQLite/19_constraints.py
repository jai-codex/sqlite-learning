import sqlite3

conn = sqlite3.connect("hackathon.db")
cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS farmers_testing(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Number TEXT UNIQUE,
    Status TEXT DEFAULT 'active'
    )""")

conn.commit()
conn.close()

print("Done!")