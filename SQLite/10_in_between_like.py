import sqlite3

conn = sqlite3.connect("hackathon.db")
cursor = conn.cursor()

cursor.execute(
    "   SELECT * FROM users WHERE name IN(?, ?, ?)",
    ("Jai", "Amit", "Arjun"))

users = cursor.fetchall()

for user in users:
    print(user)

print("-------------")

cursor.execute(
    "SELECT * FROM users WHERE age BETWEEN ? AND ?",
    (18, 20))

users = cursor.fetchall()

for user in users:
    print(user)

print("-------------")

cursor.execute(
    "SELECT * FROM users WHERE name LIKE ?",
    ("A%",))

users = cursor.fetchall()

for user in users:
    print(user)

print("-------------")

conn.close()
