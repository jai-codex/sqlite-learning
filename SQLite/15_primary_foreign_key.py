import sqlite3

connection = sqlite3.connect("hackathon.db")
cursor = connection.cursor()

# Enable foreign keys
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS farmers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS crops (
        id INTEGER PRIMARY KEY,
        crop_name TEXT NOT NULL,
        farmer_id INTEGER,
        FOREIGN KEY (farmer_id) REFERENCES farmers(id)
    )
""")

connection.commit()
connection.close()

print("Farmers and crops tables created!")