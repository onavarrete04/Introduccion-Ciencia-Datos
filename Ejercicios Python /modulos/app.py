from usuarios.gestion.impuestos.utilidades import pagar_impuestos
#    paquete.modulo            funcion

import usuarios

print(dir(usuarios))
print(usuarios.gestion.__name__)
print(usuarios.__package__)
print(usuarios.gestion.__path__)
print(usuarios.__file__)


print(__name__)

pagar_impuestos()
