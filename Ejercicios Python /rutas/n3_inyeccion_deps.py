"""Inyeccion"""

# class Perro:
#     def __init__(self, Correa):
#         self.correa = Correa()

from pathlib import Path


path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "base de datos",
    "api": "esta es la api",
    "graphql": "esto es grpahql"
}


def load(p):

    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene funcion init")


list(map(load, paths))
