import sqlite3

connection = sqlite3.connect("hackathon.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS farmer_test")

cursor.execute("""
    CREATE TABLE farmer_test (
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT
    )
""")

# Insert farmers
farmers = [
    ("Jai", "9876543210"),
    ("Rahul", "8765432109"),
    ("Amit", "7654321098"),
    ("Rohan", "9876501234"),
    ("Arjun", "9123456789")
]

cursor.executemany(
    "INSERT INTO farmer_test (name, phone) VALUES (?, ?)",
    farmers
)

# Create index on phone
cursor.execute("""
    CREATE INDEX idx_farmer_phone
    ON farmer_test(phone)
""")

connection.commit()

# Search for a farmer
cursor.execute(
    "SELECT * FROM farmer_test WHERE phone = ?",
    ("9876543210",)
)

farmer = cursor.fetchone()

print("Found farmer:")
print(farmer)

connection.close()