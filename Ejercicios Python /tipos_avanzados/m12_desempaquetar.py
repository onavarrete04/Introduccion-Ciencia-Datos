"""Desempaquetar"""

lista: list = [1, 2, 3, 4]

print(*lista)

tupla: tuple = (1, 2, 3, 4)
print(*tupla)

# El * desempaqueta

lista2: list = [5, 6]

combinada: list = [*lista, "hola", *lista2]


# DICCIONARIOS

punto1: dict = {"x": 19}
punto2: dict = {"y": 29}

print({**punto1, **punto2})

# NO PUEDE DESEMPAQUETAR UN DICCIONARIO directamente en el print
# print(**punto1)

punto3: dict = {'x': 1, 'y': 2}
lista: list = [{**punto3}]
print(lista)
