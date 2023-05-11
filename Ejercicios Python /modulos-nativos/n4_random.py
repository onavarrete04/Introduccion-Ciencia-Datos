import random
import string

lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8]

random.shuffle(lista)
print(random.random())  # entre 0 y 1
print(random.randint(1, 100))  # numero aleatorio entre 1 y 100
print(lista)
print(random.choice(lista))
print(random.choices(lista, k=4))
print(random.choices("abcdefghijk", k=4))
print("".join(random.choices("abckckdkslflhasjkhlkd", k=4)))

chars = string.ascii_letters
digitos = string.digits

seleccion = random.choices(chars+digitos, k=16)
print(seleccion)

contrasena = "".join(seleccion)
print(contrasena)
