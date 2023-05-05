"""Alcance"""

saludo: str = "Hola Global"


def saludar():
    """funcion 1"""
    global saludo
    saludo: str = "Hola Mundo"
    print(saludo)


def saluda_chanchito():
    "funcion 2"
    saludo: str = "Hola Chanchito"
    print(saludo)

# No se recomienda usar variables globales es mala práctica
