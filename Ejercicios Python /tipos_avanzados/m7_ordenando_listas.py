"""ordenando"""
import random

numeros: list = [random.randint(1, 18) for _ in range(10)]
print(numeros)
numeros.sort(reverse=True)
# sort afecta la lista anterior y se queda la nueva

print(numeros)
numeros: list = [random.randint(1, 18) for _ in range(10)]
# sorted crea una nueva lista

numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)


usuarios: list = [[4, "chanchito"], [1, "felipe"], [5, "pulta"]]
usuarios.sort()
print(usuarios)

usuarios2: list = [["chanchito", 3], ["felipe", 5], ["pulta", 2]]
# sort en este caso no ordenaria por el numero


def ordenar(elemento):
    """Ordena una lista"""
    return elemento[1]


# sort le pasa por debajo el argumento a la funcion ordenar
usuarios2.sort(key=ordenar, reverse=True)
print(usuarios2)

usuarios3: list = [["chanchito", 3], ["felipe", 5], ["pulta", 2]]

usuarios3.sort(key=lambda x: x[1])

print(usuarios3)
