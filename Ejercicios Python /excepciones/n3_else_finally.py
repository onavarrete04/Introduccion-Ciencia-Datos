"""else y finally"""

try:
    n1 = int(input("ingrese primer numero "))
except ValueError as e:
    print("Ocurrio un error, ingrese un valor adecuado :()")

else:
    # se ejecuta siempre y cuando no ocurre un error
    print("No ocurrio un error")
finally:
    # siempre se va a ejecutar
    print("se ejecuta siempre")
