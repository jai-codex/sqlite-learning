import sqlite3

connection = sqlite3.connect("hackathon.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("DROP TABLE IF EXISTS test_crops")
cursor.execute("DROP TABLE IF EXISTS test_farmers")

cursor.execute("""
    CREATE TABLE test_farmers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE test_crops (
        id INTEGER PRIMARY KEY,
        crop_name TEXT NOT NULL,
        farmer_id INTEGER,
        FOREIGN KEY (farmer_id)
            REFERENCES test_farmers(id)
            ON DELETE CASCADE
    )
""")

# Add farmers
cursor.execute(
    "INSERT INTO test_farmers (name) VALUES (?)",
    ("Jai",)
)

cursor.execute(
    "INSERT INTO test_farmers (name) VALUES (?)",
    ("Rahul",)
)

# Add crops
cursor.execute(
    "INSERT INTO test_crops (crop_name, farmer_id) VALUES (?, ?)",
    ("Wheat", 1)
)

cursor.execute(
    "INSERT INTO test_crops (crop_name, farmer_id) VALUES (?, ?)",
    ("Rice", 1)
)

cursor.execute(
    "INSERT INTO test_crops (crop_name, farmer_id) VALUES (?, ?)",
    ("Tomato", 2)
)

connection.commit()

print("Before deleting Jai:")

cursor.execute("SELECT * FROM test_crops")

for crop in cursor.fetchall():
    print(crop)

# Delete Jai
cursor.execute(
    "DELETE FROM test_farmers WHERE id = ?",
    (1,)
)

connection.commit()

print("\nAfter deleting Jai:")

cursor.execute("SELECT * FROM test_crops")

for crop in cursor.fetchall():
    print(crop)

connection.close()