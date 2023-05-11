import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()  # intermediario entre sql y las consultas
    cursor.execute(
        "insert into usuarios values(?,?)",
        (1, "Hola mundo"),



    )  # ejecuta consultas
