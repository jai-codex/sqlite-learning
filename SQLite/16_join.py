import sqlite3

connection = sqlite3.connect("hackathon.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT farmers.name, crops.crop_name
    FROM farmers
    JOIN crops
    ON farmers.id = crops.farmer_id
""")

results = cursor.fetchall()

for result in results:
    print(result)

connection.close()