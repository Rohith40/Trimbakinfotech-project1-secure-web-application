import sqlite3

# Connect to SQLite database. If the database does not exist, it will be created.
conn = sqlite3.connect('database.db')

# Execute an SQL command to create a table called 'users'
conn.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Close the connection to the database
conn.close()

print("Database and table created successfully.")
