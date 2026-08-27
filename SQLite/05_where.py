import sqlite3

conn = sqlite3.connect("hackathon.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM users WHERE age > ?",
    (18,))

users = cursor.fetchall()

for user in users:
    print(user)

conn.close()

print("Done!")