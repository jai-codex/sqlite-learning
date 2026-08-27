import sqlite3

conn = sqlite3.connect("Hackthon.db")
cursor = conn.cursor()

cursor.executemany(
    "INSERT INTO users(name, age) VALUES(?, ?)",
    [
    ("Jai", 19),
    ("Rahul", 20),
    ("Amit", 19),
    ("Rohan", 21),
    ("Arjun", 18),
    ("Vikram", 22),
    ("Aditya", 20),
    ("Karan", 19),
    ("Sahil", 21),
    ("Neeraj", 18)])

conn.commit()
conn.close()

print("Data inserted successfully!")