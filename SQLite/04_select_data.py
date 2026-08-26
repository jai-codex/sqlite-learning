import sqlite3

conn = sqlite3.connect("Hackthon.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM users")

users = cursor.fetchall()

for user in users:
    print(user)

conn.close()

print("Users displayed successfully!")