import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT id, username, password, role FROM users")
users = cursor.fetchall()

print("\nREGISTERED USERS:\n")
for user in users:
    print(f"ID: {user[0]} | Username: {user[1]} | Password: {user[2]} | Role: {user[3]}")

conn.close()
