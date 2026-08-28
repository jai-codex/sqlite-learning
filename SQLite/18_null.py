import sqlite3

conn = sqlite3.connect("hackathon.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM crops WHERE farmer_id IS NULL")

crops = cursor.fetchall()
for crop in crops:
    print(crop)

conn.close()