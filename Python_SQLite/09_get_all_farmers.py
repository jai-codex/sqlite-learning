from database import get_connection


def get_all_farmers():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM farmers")

    farmers = cursor.fetchall()

    connection.close()

    return farmers


farmers = get_all_farmers()

for farmer in farmers:
    print(farmer)