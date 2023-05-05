"""Ejercicio depuracion"""


def largo(texto: str):
    """Ejercicio"""
    resultado: int = 0

    for _ in texto:
        resultado += 1
    return resultado


print("chanchito")
l: int = largo("Hola Mundo")
print(l)
