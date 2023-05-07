"""Duckt Typing"""


class Usuario():
    def guardar(self):
        print("Guardando en BBDD")


class Sesion():
    def guardar(self):
        print("guardando en archivo")


# ya no se necesitaría model porque se usa tipado dinamico
# pero debe verificarse que entre una lista con dos elementos, entre ellos, el metodo guardar
def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()

guardar([sesion, usuario])
