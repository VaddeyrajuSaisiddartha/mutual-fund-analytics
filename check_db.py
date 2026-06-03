import sqlite3

print("Checking database...")

conn = sqlite3.connect("database/mutual_fund.db")

cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables = cursor.fetchall()

print("\nTables found:")

for table in tables:
    print(table[0])

conn.close()

print("\nDatabase check complete!")