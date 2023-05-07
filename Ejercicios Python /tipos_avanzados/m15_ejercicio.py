"""Eliminar espacios en blaco de un string"""


def eliminar(texto: str):
    """Eliminando espacios vacios"""
    palabra: str = ""
    for char in texto:
        if char != " ":
            palabra = palabra + char
    print(palabra)


def elimino(texto: str):
    """Funcion 2 de eliminar"""
    print(texto.replace(" ", ""))


eliminar("Hola Mundo")
elimino("  Hola Mundo ")
print("--"*8)

# utilizando filter para agregar los que no estan vacios

palabra: str = " hola mundo "
lista = list(filter(lambda char: char != " ", palabra))
print(lista)

# anidada para agregar a los que no estan vacios


def eliminar_espacios(texto: str):
    """
    Funcion listas anidadas

    """
    lista_caracteres: list = [char for char in texto if char != " "]
    print(lista_caracteres)


eliminar_espacios("Hola Mundo Chanchito Feliz")
