import sqlite3

conn = sqlite3.connect("Hackthon.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM users ORDER BY age DESC LIMIT 2")

users = cursor.fetchall()

for user in users:
    print(user)

conn.close()