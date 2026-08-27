import sqlite3

conn = sqlite3.connect("hackathon.db")

print("Database created successfully!")

conn.close()