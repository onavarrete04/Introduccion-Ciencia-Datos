"""Tuplas"""

# las tuplas no se pueden modificar, ni agregar, ni quitar elementos, pero se pueden
# crear tuplas con ya existentes.

numeros: tuple = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto: list = [1, 2]

punto: tuple = tuple(punto)
print(punto)

primero, segundo, *otros = numeros

print(primero, segundo, otros)

# asi se modifica una tupla, que escreando una lista en base a la tupla
# pero a la final la tupla será la misma.

listaNumero = list(numeros)
