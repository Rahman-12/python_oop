import sqlite3 
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute("""create table if not exists people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INT
                )
""")
connection.commit()


cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", ("Ali", 25))
cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", ("Umair", 30))

connection.commit()


connection.close()