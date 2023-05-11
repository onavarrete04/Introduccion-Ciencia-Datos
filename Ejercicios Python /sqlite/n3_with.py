import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()  # intermediario entre sql y las consultas
    cursor.execute(
        """
    CREATE TABLE if not exists usuarios
    (id INTEGER primary key, nombre VARCHAR(50));

    """


    )  # ejecuta consultas
