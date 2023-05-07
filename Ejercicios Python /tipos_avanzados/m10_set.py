"""Conjunto o grupo"""

primer: set = {1, 1, 2, 2, 3, 4}  # da amarillo porque hay datos duplicados

print(primer)

# los set se trabaja como en las listas

primer.add(5)
primer.remove(1)
print(primer)

segundo: list = [3, 4, 5]
segundo: set = set(segundo)

print(segundo)

# OPERADORES PYTHON

# UNIÓN

print(primer | segundo)

# INTERSECCIÓN
print(primer & segundo)

# DIFERENCIA

print(primer - segundo)

# DIFERENCIA SIMETRICA
print(primer ^ segundo)

# no se encuentran ordenados

if 5 in segundo:
    print("hola mundo")
