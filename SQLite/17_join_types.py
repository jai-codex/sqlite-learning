import sqlite3

conn = sqlite3.connect("hackathon.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT farmers.name, crops.crop_name FROM farmers INNER JOIN crops ON farmers.id = crops.farmer_id")

results = cursor.fetchall()
for result in results:
    print(result)

print("----------------")

cursor.execute(
    "SELECT farmers.name, crops.crop_name FROM farmers LEFT JOIN crops ON farmers.id = crops.farmer_id")

results = cursor.fetchall()
for result in results:
    print(result)

conn.close()    