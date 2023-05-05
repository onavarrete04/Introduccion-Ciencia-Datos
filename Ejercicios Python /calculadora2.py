"""Ejercicio calculadora 2"""

# if not esta indicando que si es falso si es None, 0, string vacio o False
# entonces si el valor es falso vamos a entrar

resultado: str = ""


print("Para salir escriba salir")
while True:

    if not resultado:
        resultado = input("ingrese el primer numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op: str = input(
        "ingrese una opción: suma, resta, division, multiplicacion: ")

    if op.lower() == "salir":
        break
    n2: str = input("ingrese otro numero: ")
    if n2.lower == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2

    elif op.lower() == "division":
        resultado /= n2

    elif op.lower() == "multiplicacion":
        resultado *= n2

    else:
        print("operacion no valida")
        break

    print(resultado)
