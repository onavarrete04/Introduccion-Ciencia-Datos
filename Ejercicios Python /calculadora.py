"""Calculadora"""

n1 = int(input("ingrese"))
n2 = int(input("ingresa el segundo numero"))

print(n1 + n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""

Para los numeros {n1} y {n2} el resultado de la suma es {suma}.
Para los numeros {n1} y {n2} el resultado de la resta es {resta}.
Para los numeros {n1} y {n2} el resultado de la multiplicacion es {multiplicacion}.
Para los numeros {n1} y {n2} el resultado de la division es {division}.
"""
print(mensaje)

print(bool(""))  # falso

print(bool("0"))  # verdadero

print(bool("None"))  # falso

print(bool(1))  # verdadero

print(bool(0))  # falso
print(2 < 1)  # se marca con ... por redundancia


edad: int = 22

if edad > 17:
    print("Puede ver la pelicula")
