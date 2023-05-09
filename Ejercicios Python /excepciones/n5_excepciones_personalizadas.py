"""Personalizadas"""


class Errores(Exception):
    "Esta clase es para representar mi error"

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):

        return f"{self.mensaje} - código {self.codigo}"


def division(n=0):
    """No se puede dividir por cero"""
    if n == 0:
        raise Errores("No se puede dividir por cero", 805)
    return 5/n


try:
    division()
except Errores as e:
    print(e)
