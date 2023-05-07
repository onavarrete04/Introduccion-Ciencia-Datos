"""Metodos clase"""


class Perro:
    """Creando el constructor"""

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        """Devuelve el valor del nombre"""
        return self.__nombre

    def set_nombre(self, nombre):
        """Modifica el nombre"""
        self.__nombre = nombre

    def habla(self):
        """Ladra"""
        print("{self.__nombre} dice Guau")

    @classmethod
    def factory(cls):
        """Creador de objetos"""
        return cls("Chanchito Feliz", 4)


perro1 = Perro("Chanchito", 2)
perro2 = Perro("Miguelito", 3)
perro3 = Perro.factory()
print(perro3.edad)
