"""Metodos magicos

Un metodo magico se llama automaticamente solo
sin necesidad de que nosotros lo hagamos
"""


class Perro:
    """Clase perro"""

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        """imprime nombre y guau"""
        print(f"{self.nombre} dice guau")


perro = Perro("Chanchito", 7)
print(perro)  # imprime y llama al metodo main y el nombre del objeto

# también puede utilizarse con los metodos magicos para crear variables
texto = "Hola mundo " + str(perro)
print(texto)
