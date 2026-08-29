from database import get_connection

def add_farmer(Name, Phone):
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO farmers(Name, Phone) VALUES(?, ?)",
        (Name, Phone))

    conn.commit()
    conn.close()

add_farmer("Jai", 101)
add_farmer("Shree", 102)
add_farmer("Gopi", 103)

print("Added to table!")