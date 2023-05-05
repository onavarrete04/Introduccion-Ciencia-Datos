"""Buscar elementos"""

mascotas: list = ["Wolfgang", "Pelula", "Pulga", "Wolfgang",
                  "Wolfgang", "Felipe", "Chanchito Feliz"]
print(mascotas.count("Wolfgang"))
if "Wolfgang" in mascotas:
    print(mascotas.index("Wolfgang"))
    print(mascotas.count("Wolfgang"))
