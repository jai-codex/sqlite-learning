import sqlite3

conn = sqlite3.connect("hackathon.db")
cursor = conn.cursor()

cursor.execute(
    "INSERT OR IGNORE INTO farmers (name) VALUES(?)",
    ("Jai",))

cursor.execute(
    "INSERT OR IGNORE INTO farmers (name) VALUES(?)",
    ("Shree",))

cursor.execute(
    "INSERT OR IGNORE INTO crops (crop_name, farmer_id) VALUES (?, ?)",
    ("Wheat", 1)
)

cursor.execute(
    "INSERT OR IGNORE INTO crops (crop_name, farmer_id) VALUES (?, ?)",
    ("Rice", 1)
)

cursor.execute(
    "INSERT OR IGNORE INTO crops (crop_name, farmer_id) VALUES (?, ?)",
    ("Tomato", 2)
)

conn.commit()
conn.close()