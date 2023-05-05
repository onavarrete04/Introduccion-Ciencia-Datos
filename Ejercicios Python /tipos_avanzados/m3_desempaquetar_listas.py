"""Desempaquetar"""

numeros: list = [1, 2, 3]

primero, segundo, tercero = numeros

first, *otros = numeros
print(primero)
print(otros)

fist, *otros, ultimo = numeros

print(first, otros, ultimo)
