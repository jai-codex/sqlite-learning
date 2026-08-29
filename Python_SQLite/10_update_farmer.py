from database import get_connection

def update_farmer(ID, Name, Phone):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE farmers SET Name=?, Phone=? WHERE ID=?",
        (Name, Phone, ID))

    conn.commit()
    conn.close()

update_farmer(1, "Mayur", 100)
        
print("Table updated!")