import sqlite3

connection = sqlite3.connect("pets.db") # Connect to database

# Cursor is a window to comunicate with the database, must be opened before executing operations, after that, must be closed
cursor = connection.cursor() # create cursor

# create table if not exists
cursor.execute("CREATE TABLE IF NOT EXISTS pet(id INTEGER PRIMARY KEY, name VARCHAR(255) UNIQUE, age REAL)") # Operation - Create a Table called pets with fields:
# field_name, type, size;
# id, INTEGER,
# name, VARCHAR, 255
# age, REAL,

# Get all pets of pet table
pets = cursor.execute("SELECT * FROM pet").fetchall()
print("pets before insertion: ", pets)
# insert pet into pet table
cursor.execute("INSERT INTO pet(name, age) VALUES('aquiles', 7.5)")
# Get all pets of pet table
pets = cursor.execute("SELECT * FROM pet").fetchall()
print("pets after insertion: ", pets)
# update specific rows
cursor.execute("UPDATE pet SET age = 21.2 WHERE name = 'aquiles'")

# Search for specific pet
print("after update: ", cursor.execute("SELECT * FROM pet WHERE name = 'aquiles'").fetchone())

# delete pet from table bet
cursor.execute("DELETE FROM pet WHERE  name = 'aquiles' LIMIT 1")
print("afte delete: ", cursor.execute("SELECT * FROM pet WHERE name = 'aquiles'").fetchone())

# list tables of database
tables = [table[0] for table in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()]
print("tables:", tables)

# drop all tables of database
for table in tables:
    cursor.execute(f"DROP TABLE {table}").fetchall()

# list tables of database
tables = [table[0] for table in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()]
print("tables:", tables)

cursor.close() # close cursor
connection.commit() # etch changes on database
connection.close() # clone connection