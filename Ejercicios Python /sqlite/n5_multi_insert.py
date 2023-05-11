import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()  # intermediario entre sql y las consultas
    usuarios = [
        (2, "Chanchito feliz"),
        (3, "Chanchito Triste"),
        (4, "Chanchango")

    ]
    cursor.executemany(
        "insert into usuarios values(?,?)",
        usuarios,
    )
