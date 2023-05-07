"""Diccionarios"""

# Llaves y Valor
# las llaves siempre son strings

punto: dict = {"x": 25, "y": 50}
print(punto["x"])  # se accede mediante las llaves


punto["z"] = 45
print(punto)

if "lala" in punto:
    print("hola mundo")


# GET

print(punto.get("x"))
print(punto.get("lala"))

# si no existiera se puede crear

print(punto.get("lala", 97))

# eliminar un elemento

del punto["x"]
print(punto)

punto["x"] = 25

for i in punto:
    print(i)  # devuelve las llaves

for i in punto:
    print(punto[i])

# esto devuelve tuplas
for i in punto.items():
    print(i)

print("---")
for llave, valor in punto.items():
    print(llave, valor)

# USO REAL DE DICCIONARIOS

usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Felipe"},
    {"id": 4, "nombre": "Nicolas"},

]

for usuario in usuarios:
    print(usuario["nombre"])
