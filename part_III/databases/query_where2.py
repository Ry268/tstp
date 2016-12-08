import sqlite3

# Connect to your database.
conn = sqlite3.connect('my_store.db')

# Add a row of data.
data = conn.execute("SELECT* FROM PRODUCT WHERE title='The Pragmatic Programmer'")

for item in data:
    print(item)

conn.close()
