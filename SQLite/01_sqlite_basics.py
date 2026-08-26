import sqlite3

conn = sqlite3.connect("Hackthon.db")

print("Database created successfully!")

conn.close()