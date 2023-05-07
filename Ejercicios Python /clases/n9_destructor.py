"""Destructor"""
"""Metodos magicos

Destructor metodo magico
"""


class Perro:
    """Clase perro"""

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Chao perro )")

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        """imprime nombre y guau"""
        print(f"{self.nombre} dice guau")


perro = Perro("Chanchito", 7)
print(perro)  # imprime y llama al metodo main y el nombre del objeto
del perro
