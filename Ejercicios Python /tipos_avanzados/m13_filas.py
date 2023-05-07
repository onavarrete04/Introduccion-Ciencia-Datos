"""Filas"""
from collections import deque

lista: list = [1, 2, 3, 4]

fila = deque(lista)
fila.append(5)
fila.append(6)
print(fila)

# eliminar elementos

fila.popleft()
print(fila)

if not fila:
    print("fila")
