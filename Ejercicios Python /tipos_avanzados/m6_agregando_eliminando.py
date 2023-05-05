"""Hola"""
mascotas: list = ["Wolfgang", "Pelula", "Pulga", "Wolfgang",
                  "Wolfgang", "Felipe", "Chanchito Feliz"]

mascotas.insert(1, "Drako")
print(mascotas)

mascotas.append("Mafalda")

print(mascotas)


mascotas.remove("Wolfgang")  # elimina el primero
mascotas.pop()  # borra el ultimo elemento o se le pasa el index
del mascotas[0]  # elimina con del
mascotas.clear()  # borra todo
