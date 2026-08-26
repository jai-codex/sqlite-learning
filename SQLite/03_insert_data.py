import sqlite3

conn = sqlite3.connect("Hackthon.db")
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO users(name, age) VALUES(?, ?)",
    ("Jai", 19))

conn.commit()
conn.close()

print("Data inserted successfully!")