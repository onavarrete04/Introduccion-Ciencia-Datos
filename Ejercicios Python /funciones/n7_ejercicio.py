"""Ejercicio"""

# forma 1 para hacer ambas cosas


def es_palindromo(texto: str):
    """
    Recibe el parametro texto
    se escribe exactamento igual
    """
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]


print(es_palindromo("SomOs o No Somos"))

# forma 2 para ordenar la palabra al reves

palabra: str = "Hola Mundo"
palabra_2: str = ""

for i in range(1, len(palabra)+1):
    palabra_2 += palabra[-i]
print(palabra_2)

# forma 3 para hacerlo de manera sencilla

a: str = ""

for char in palabra:
    if char != " ":
        a = char + a
print(a)
