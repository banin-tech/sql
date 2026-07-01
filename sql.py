import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Username: ")

query = "SELECT * FROM users WHERE username = '" + username + "'"

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

conn.close()
