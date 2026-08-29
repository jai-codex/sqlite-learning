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
        print("Farmer added!")

    except sqlite3.IntegrityError as error:
        print("Error:", error)

    finally:
        connection.close()


def get_all_farmers():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM farmers")

    farmers = cursor.fetchall()

    connection.close()

    return farmers


def update_farmer(farmer_id, name, phone):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE farmers
        SET name = ?, phone = ?
        WHERE id = ?
        """,
        (name, phone, farmer_id)
    )

    connection.commit()
    connection.close()

    print("Farmer updated!")


def delete_farmer(farmer_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM farmers WHERE id = ?",
        (farmer_id,)
    )

    connection.commit()
    connection.close()

    print("Farmer deleted!")


# CREATE
add_farmer("Demo Farmer", "1111111111")


# READ
print("\nAll farmers:")

for farmer in get_all_farmers():
    print(farmer)


# UPDATE
update_farmer(
    1,
    "Jai Updated",
    "9999999999"
)


# DELETE
delete_farmer(2)


# READ again
print("\nFarmers after changes:")

for farmer in get_all_farmers():
    print(farmer)