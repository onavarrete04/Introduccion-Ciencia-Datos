from io import open

# Escritura

# texto = "Hola mundo"
# archivo = open("archivos/hola_mundo.txt", "w")
# archivo.write(texto)
# archivo.close()

# archivo = open("archivos/hola_mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)


# archivo = open("archivos/hola_mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)


# with y seek, seek hace la posición del caracter
# with open("archivos/hola_mundo.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# agregar

# archivo = open("archivos/hola_mundo.txt", "a+")
# archivo.write(" Chao Mundo :(")
# archivo.close()

# lectura y escritura

with open("archivos/hola_mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito Felix"
    archivo.writelines(texto)
