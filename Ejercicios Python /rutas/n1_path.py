"""RUTAS"""

from pathlib import Path
# sirve para referenciar una ruta dentro del pc


# Path("/usr/bin")
# Path()
# Path.home()
# Path("one/__init__.py")

path = Path("Hola_Mundo/mi_archivo.py")
path.is_file()  # saber si es un archivo
path.is_dir()  # saber si es un directorio
path.exists()  # saber si existe

print("--"*3,
      path.name,
      path.stem,
      path.suffix,
      path.parent,
      path.absolute()
      )


p = path.with_name("Chanchito.py")
print(p)
p = path.with_suffix(".bat")
print(p)
# p = path.with_stem("feliz") # esta es de la version desde la 3.9
# print(p)
