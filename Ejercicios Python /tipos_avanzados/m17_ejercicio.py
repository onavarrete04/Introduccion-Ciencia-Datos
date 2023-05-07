"""Funcion"""


def diccionario_contador(texto: str):
    """Cuenta caracteres y crea un diccionario con los caracteres"""

    diccionario = {}

    for caracter in texto:
        if caracter in diccionario:
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1
    print(diccionario)


diccionario_contador("lalaaaab")
