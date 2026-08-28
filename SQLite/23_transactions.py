import sqlite3

connection = sqlite3.connect("hackathon.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS accounts")

cursor.execute("""
    CREATE TABLE accounts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        balance INTEGER
    )
""")

cursor.execute(
    "INSERT INTO accounts (name, balance) VALUES (?, ?)",
    ("Jai", 1000)
)

cursor.execute(
    "INSERT INTO accounts (name, balance) VALUES (?, ?)",
    ("Rahul", 500)
)

connection.commit()

print("Before transfer:")

cursor.execute("SELECT * FROM accounts")
for account in cursor.fetchall():
    print(account)

# Start transaction
try:
    cursor.execute(
        "UPDATE accounts SET balance = balance - ? WHERE name = ?",
        (200, "Jai")
    )

    cursor.execute(
        "UPDATE accounts SET balance = balance + ? WHERE name = ?",
        (200, "Rahul")
    )

    connection.commit()

    print("\nTransfer successful!")

except Exception:
    connection.rollback()
    print("\nTransfer failed!")

print("\nAfter transfer:")

cursor.execute("SELECT * FROM accounts")
for account in cursor.fetchall():
    print(account)

connection.close()