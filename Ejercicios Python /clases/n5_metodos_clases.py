"""Metodos clase"""


class Perro:
    """Creando el constructor"""
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        """Ladra"""
        print("dice Guau")

    @classmethod
    def factory(cls):
        """Creador de objetos"""
        return cls("Chanchito Feliz", 4)


Perro.habla()
perro1 = Perro("Chanchito", 2)
perro2 = Perro("Miguelito", 3)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)
