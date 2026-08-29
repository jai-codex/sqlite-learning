from database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS farmers(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    phone TEXT UNIQUE NOT NULL)""")

conn.commit()
conn.close()

print("Table created successfully!")