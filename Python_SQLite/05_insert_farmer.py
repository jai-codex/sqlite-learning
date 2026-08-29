from database import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute(
    "INSERT INTO farmers (name, phone) VALUES (?, ?)",
    ("Jai", "9876543210")
)

connection.commit()
connection.close()

print("Farmer added successfully!")
