""" Ejercicio  """
edad: int = 15

if edad > 17:
    mensaje: str = "Es mayor"

else:
    mensaje: str = "Es menor"

print(mensaje)

mensaje: str = "Es mayor" if edad > 17 else "es menor"
print(mensaje)

gas: bool = True
encendido: bool = True
edad: int = 18

if gas and encendido and edad > 17:
    print("puedes avanzar")

# se entiende como si el auto no tiene gas y esta encendido
if not gas and encendido:
    print("puedes avanzar por 2")

# operadores de corto circuito

if not gas and encendido and edad > 17:
    print("puedes avanzar por 3")
