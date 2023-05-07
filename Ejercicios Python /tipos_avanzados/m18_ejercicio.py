"""Ejercicio"""


def lista_tuplas(diccionario: dict):
    """ devuelve un diccionario con tuplas """

    diccionario: dict = dict(
        sorted(diccionario.items(), key=lambda llave: llave[1], reverse=True))
    print(diccionario)


lista_tuplas({"a": 2, "b": 2, "c": 3, "d": 1})
print("--"*2)


def mayor_tupla(lista_tupla: tuple):
    """Tuplas """
    nueva_lista = []
    contador = lista_tupla[0][1]

    for tupla in lista_tupla:
        if tupla[1] > contador:
            contador = tupla[1]

    for tupla in lista_tupla:
        if contador == tupla[1]:
            nueva_lista.append(tupla)
            print(
                f"""los cáracteres que más se repiten son \n 
                {tupla[1]} de la letra {tupla[0].capitalize()}""")

    print(nueva_lista)


lista1 = [("b", 8), ("c", 4), ("z", 9)]
mayor_tupla(lista1)
