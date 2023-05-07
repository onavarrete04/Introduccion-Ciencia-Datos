"""
Contar en un diccionario cuanto se repiten elementos

"""


def contador_diccionario(diccionario: dict):
    """
    cuenta elementos
    """
    for llave, valor in diccionario.items():
        print(llave, len(valor))


a = {"a": "aa", "b": "aaa"}
contador_diccionario(a)

print("---")


def contador(diccionario):
    """Hey"""
    contar: int = 0
    for llave in diccionario.items():
        for _ in llave[1]:
            contar += 1
        print(llave[0], contar)
        contar = 0


contador(a)
