import sqlite3

connection = sqlite3.connect("hackathon.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT name, age
    FROM users
    WHERE age > (SELECT AVG(age) FROM users)
""")

users = cursor.fetchall()

for user in users:
    print(user)

connection.close()