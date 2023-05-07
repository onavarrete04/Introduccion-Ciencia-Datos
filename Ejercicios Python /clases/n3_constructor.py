"""constructor"""


class Perro:
    """Creando el constructor"""

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        """Ladra"""
        print(f"{self.nombre} dice Guau")


mi_perro = Perro("Chanchito", 3)
mi_perro_2 = Perro("Chancho", 4)
print(mi_perro.nombre)
print(mi_perro_2.habla())
