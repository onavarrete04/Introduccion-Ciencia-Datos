"""Return"""


def suma(numero1: int, numero2: int):
    """aplicando return"""
    resultado = numero1 + numero2
    return resultado


c: int = suma(1, 2)
d: int = suma(c, 4)  # se pasa una función

print(d)
