"""
Busca elementos
operaciones matematicas
crea elementos nuevos

"""

for numero in range(5):
    print(numero, numero * "hola mundo")

buscar: int = 10

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontro el numero buscado")


for char in "Ultime python":
    print(char)
