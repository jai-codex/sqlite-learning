from database import get_connection

def delete_farmer(ID):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM farmers WHERE ID=?",
        (ID,))

    conn.commit()
    conn.close()

delete_farmer(1)
print("Farmer delete successfully!")


