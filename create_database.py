import sqlite3

conn = sqlite3.connect("database/mutual_fund.db")

with open("sql/schema.sql", "r") as file:
    schema = file.read()

conn.executescript(schema)

conn.commit()
conn.close()

print("Database created successfully!")