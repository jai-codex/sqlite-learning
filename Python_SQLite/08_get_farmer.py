from database import get_connection

def get_farmer(ID):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM farmers WHERE ID=?",
        (ID,))

    farmer = cursor.fetchone()

    conn.close()
    return farmer

farmer = get_farmer(1)
print(farmer)

farmer = get_farmer(3)
print(farmer)