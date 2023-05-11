import sqlite3

con = sqlite3.connect("sqlite/app.db")
cursor = con.cursor()  # intermediario entre sql y las consultas
cursor.execute(
    """
CREATE TABLE if not exists usuarios
(id INTEGER primary key, nombre VARCHAR(50));

"""


)  # ejecuta consultas
con.commit()  # commit permite realizar los cambios
con.close()
