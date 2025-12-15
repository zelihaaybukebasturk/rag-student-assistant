import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

c.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)",
          ("teacher1", "1234", "teacher"))

conn.commit()
conn.close()

print("Users DB created successfully.")
