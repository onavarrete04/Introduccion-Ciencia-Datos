from pathlib import Path
from zipfile import ZipFile

# Escribir

# with ZipFile("archivos/comprimidos.zip", "w") as zip:
#     for path in Path().rglob("*.*"):
#         print(path)
#         if str(path) != "archivos/comprimidos.zip":
#             zip.write(path)

# Leer

with ZipFile("archivos/comprimidos.zip") as zip:
    # print(zip.namelist())

    # buscar por archivo especifico
    info = zip.getinfo("archivos/n6_comprimidos.py")
    print(
        info.file_size,
        info.compress_size
    )
    zip.extractall("archivos/descomprimidos")
