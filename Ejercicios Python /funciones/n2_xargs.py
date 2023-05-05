"""xargs cuando no se sabe cuantos argumentos se van a pasar"""


# def suma(numero_1: int, numero_2: int):
#     """Vamos a sumar"""
#     print(numero_1 + numero_2)


def suma_1(*numeros_de_entrada: int):
    """Suma"""
    resultado = 0
    for numero in numeros_de_entrada:
        resultado += numero
    print(resultado)


suma_1(1, 2, 3, 4, 5.1)

# el * convierte en iterables los numeros de entrada
