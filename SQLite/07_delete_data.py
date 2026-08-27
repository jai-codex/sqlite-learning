import sqlite3

conn = sqlite3.connect("hackathon.db")
cursor = conn.cursor()

cursor.execute(
    "DELETE FROM users WHERE name=?",
    ("Amit",))

conn.commit()
conn.close()

print("Delete successfully!")
