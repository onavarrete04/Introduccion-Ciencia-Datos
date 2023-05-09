"""Tipos de excepciones"""
"""Capturan excepciones"""

try:
    n1 = int(input("ingrese primer numero "))
except ValueError as e:
    print("Ocurrio un error, ingrese un valor adecuado :()")

# para este caso entonces lo que se hace en un principio
# es llamar a Exception la clase que toma todos los errores
# se imprime el type(e) se obtiene el error y luego se le pasa
# el error especifico
