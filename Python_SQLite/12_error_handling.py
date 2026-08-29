from database import get_connection
import sqlite3


def add_farmer(name, phone):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO farmers (name, phone) VALUES (?, ?)",
            (name, phone)
        )

        connection.commit()
        print("Farmer added successfully!")

    except sqlite3.IntegrityError:
        print("Error: Phone number already exists or value is missing.")

    finally:
        connection.close()


add_farmer("Test User", "9876543210")