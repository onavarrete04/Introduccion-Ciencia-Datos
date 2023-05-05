"""Listas"""

usuarios3: list = [["chanchito", 3], ["felipe", 5], ["pulta", 2]]

nombres: list = []
for usuario in usuarios3:
    nombres.append(usuario[0])

# transformar  esto de trnasformar una lista se conoce como map
nombres2 = [usuario[0] for usuario in usuarios3]

# [expresin de lo que se quiere for variable en iterador]
print(nombres2)

# entonces se puede hacer lo mismo filtrando asi esta se puede conocer como filter

nombres3 = [usuario for usuario in usuarios3 if usuario[1] > 2]
print(nombres3)

# esta sería map y filter en una sola
nombres4 = [usuario[0] for usuario in usuarios3 if usuario[1] > 2]
print(nombres4)


# metodo map y filter

nombres = list(map(lambda: usuario usuario[0], usuarios3))