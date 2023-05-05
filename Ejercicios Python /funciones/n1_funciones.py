"""Funciones"""


def hola(nombre: str):
    """Ejercicio 1"""
    print("Hola Mundo")
    print(f"Bienvenido {nombre}")


hola("Oscar")

a: list = [1, 2, 3, 4, 2]

contador: int = 0
for elemento in a:
    if elemento == 2:
        contador += 1

if contador > 0:
    print("Verdadero " * contador)

hola("Camila")

# Funciones con párametros opcionales


def hola1(nombre: str, apellido: str = "Feliz"):
    """Ejercicio 1"""
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")


hola1("Camila")

hola1("Oscar", "Navarrete")

#

hola1(apellido="Peña", nombre="Angela")
