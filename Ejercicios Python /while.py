"""while"""

# numero: int = 1

# while numero < 100:
#     print(numero)
#     numero *= 2

comando: str = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

# loop anidado

for j in range(3):
    for k in range(2):
        print(j, k)
# en este anidado se ejecuta j 1 vez, mientras k se ejecuta 2
