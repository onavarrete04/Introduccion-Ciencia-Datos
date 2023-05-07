"""Decorador properties"""


class Perro:

    """Clase perro decorador"""

    def __init__(self, nombre):
        """Constructor"""
        self.nombre = nombre

    @property
    def nombre(self):
        """propiedad"""
        print("pasando por getter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        """Comprobador nombre no vacio"""
        print("pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro(" a")
print(perro.nombre)
