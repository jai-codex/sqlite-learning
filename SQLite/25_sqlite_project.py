import sqlite3

connection = sqlite3.connect("farmer_market.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Farmers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS farmers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT UNIQUE NOT NULL
)
""")

# Crops table
cursor.execute("""
CREATE TABLE IF NOT EXISTS crops (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_name TEXT NOT NULL,
    farmer_id INTEGER NOT NULL,
    FOREIGN KEY (farmer_id) REFERENCES farmers(id)
)
""")

# Offers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS offers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_id INTEGER NOT NULL,
    quantity REAL NOT NULL,
    price REAL NOT NULL,
    FOREIGN KEY (crop_id) REFERENCES crops(id)
)
""")

# Insert farmers
cursor.execute(
    "INSERT INTO farmers (name, phone) VALUES (?, ?)",
    ("Jai", "9876543210")
)

cursor.execute(
    "INSERT INTO farmers (name, phone) VALUES (?, ?)",
    ("Rahul", "8765432109")
)

# Insert crops
cursor.execute(
    "INSERT INTO crops (crop_name, farmer_id) VALUES (?, ?)",
    ("Wheat", 1)
)

cursor.execute(
    "INSERT INTO crops (crop_name, farmer_id) VALUES (?, ?)",
    ("Rice", 2)
)

# Insert offers
cursor.execute(
    "INSERT INTO offers (crop_id, quantity, price) VALUES (?, ?, ?)",
    (1, 100, 2500)
)

cursor.execute(
    "INSERT INTO offers (crop_id, quantity, price) VALUES (?, ?, ?)",
    (2, 200, 3000)
)

connection.commit()

# Show farmer + crop + offer
cursor.execute("""
SELECT farmers.name, crops.crop_name, offers.quantity, offers.price
FROM farmers
JOIN crops ON farmers.id = crops.farmer_id
JOIN offers ON crops.id = offers.crop_id
""")

results = cursor.fetchall()

for result in results:
    print(result)

connection.close()