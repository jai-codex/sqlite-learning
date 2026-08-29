from database import get_connection

def add_farmer(name, phone):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO farmers(name, phone) VALUES(?, ?)",
        (name, phone))

    conn.commit()
    conn.close()

    print("Farmer add successfully!")    