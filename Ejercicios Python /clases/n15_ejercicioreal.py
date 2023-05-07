
class Model:
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, definir tabla")

    def guardar(self):
        print(f"guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)
