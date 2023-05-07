"""Clases abstractas"""
from abc import ABC, abstractmethod


class Model(ABC):

    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("guardando usuario")


# model = Model()
# Model.buscar_por_id(123)
# esto no es correcto por eso se importa el metodo y se creo uno nuevo

usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)  # este debe ser desde la clase
