#  SQLite is very lightweight database that we use for storing data of an application its often the technology of choice for
#small applications like the apps that we run on phones and tablets. So it allows us to easily store our data in a structure 
#format with a tableof rows and columns.so lets start by importing.
import sqlite3
import json
from pathlib import Path

# created coonection to data base and inserted values
"""
movies = json.loads(Path("movies.json").read_text())
with sqlite3.connect("db.sqlite3") as conn:
    Command = "INSERT INTO Movies VALUES(?,?,?)"
    for movie in movies:
        conn.execute(Command,tuple(movie.values()))
    conn.commit()
"""
#Read data from the database
with sqlite3.connect("db.sqlite3") as conn:
     command= "SELECT * FROM Movies"
     cursor = conn.execute(command)
     #for row in cursor:
     #   print(row)
#instead of using for loop we can use below code.
     movies= cursor.fetchall()
     print(movies)
     



