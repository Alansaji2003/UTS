import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('UTS.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table with a boolean column
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY,
#         first_name TEXT NOT NULL,
#         last_name TEXT NOT NULL,
#         email TEXT NOT NULL,
#         password TEXT NOT NULL
#     )
# ''')

# Insert data with boolean column
# cursor.execute("INSERT INTO tasks (task_name, is_completed) VALUES (?, ?)", ('Task 1', 0))  # 0 for false
# cursor.execute("INSERT INTO tasks (task_name, is_completed) VALUES (?, ?)", ('Task 2', 1))  # 1 for true

# Commit the changes to the database
conn.commit()

# Query the data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print(rows)

# # Print the results
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()