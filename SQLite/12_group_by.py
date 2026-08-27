import sqlite3

conn = sqlite3.connect("hackathon.db")
cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS products(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Category TEXT,
    Price INTEGER)""")

products = [
    ("Rice", "Grain", 50),
    ("Wheat", "Grain", 40),
    ("Apple", "Fruit", 120),
    ("Mango", "Fruit", 100),
    ("Potato", "Vegetable", 30),
    ("Tomato", "Vegetable", 40)
]

cursor.executemany(
    "INSERT INTO products (Name, Category, Price) VALUES(?, ?, ?)",
    products)

conn.commit()

print("---------")

cursor.execute(
    "SELECT Category, COUNT(*) FROM products GROUP BY Category")

results = cursor.fetchall()

for result in results:
    print(result)

print("---------")

cursor.execute(
    "SELECT Category, AVG(Price) FROM products GROUP BY Category")

results = cursor.fetchall()

for result in results:
    print(result)    

conn.close()
