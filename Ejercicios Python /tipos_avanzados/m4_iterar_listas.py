"""Iterar"""

mascotas: list = ["Pelula", "Pulga", "Felipe", "Chanchito Feliz"]

for mascota in enumerate(mascotas):
    print(mascota)

# devuelve una tupla

for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
