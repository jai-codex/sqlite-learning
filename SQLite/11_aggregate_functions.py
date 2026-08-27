import sqlite3

conn = sqlite3.connect("Hackthon.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM users")
print("Total Students:", cursor.fetchone()[0])

cursor.execute(
    "SELECT AVG(age) FROM users")
print("Average Age:", cursor.fetchone()[0])

cursor.execute(
    "SELECT MIN(age) FROM users")
print("Minimum Age:", cursor.fetchone()[0])

cursor.execute(
    "SELECT MAX(age) FROM users")
print("Maximum Age", cursor.fetchone()[0])

cursor.execute(
    "SELECT SUM(age) FROM users")
print("Sum of Age:", cursor.fetchone()[0])
    
conn.close()