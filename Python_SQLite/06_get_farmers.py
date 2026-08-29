from database import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute("SELECT * FROM farmers")

farmers = cursor.fetchall()

for farmer in farmers:
    print(farmer)

connection.close()