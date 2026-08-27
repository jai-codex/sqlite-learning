import sqlite3

connection = sqlite3.connect("Hackthon.db")
cursor = connection.cursor()

cursor.execute(
    "SELECT category, COUNT(*) FROM products GROUP BY category HAVING COUNT(*) >= 2")

results = cursor.fetchall()

for result in results:
    print(result)

connection.close()
