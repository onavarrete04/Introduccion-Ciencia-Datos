"""Pilas"""

pila: list = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
ultimo = pila.pop()
print(ultimo)
pila.pop()
pila.pop()
if not pila:
    print("Pila Vacia")
