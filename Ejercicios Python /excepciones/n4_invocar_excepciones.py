"""invocando"""


def division(n=0):
    """No se puede dividir por cero"""
    if n == 0:
        raise ZeroDivisionError("No se puede dividir por cero", f"{n}")
    return 5/n


try:
    division()
except ZeroDivisionError as e:
    print(e)
