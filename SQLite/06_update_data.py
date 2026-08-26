import sqlite3

conn = sqlite3.connect("Hackthon.db")
cursor = conn.cursor()

cursor.execute(
    "UPDATE users SET age=? WHERE name=?",
    (20, "Jai"))

cursor.execute(
    "UPDATE users SET age=?, name=? WHERE ID=?",
    (100, "Shree", 1)
)

conn.commit()
conn.close()

print("Updated successfully!")