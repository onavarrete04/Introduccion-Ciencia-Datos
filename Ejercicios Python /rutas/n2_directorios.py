from pathlib import Path

# path = Path("directorio")
# path.exists()  # ver si existe
# path.mkdir()  # crea el directorio
# path.rmdir()  # elimina el directorio vacio
# path.rename("Chanchito")

path = Path("rutas")

for p in path.iterdir():
    print(p)


lista_directorios = [p for p in path.iterdir() if not p.is_dir()]
print(lista_directorios)

lista_archivos = [p for p in path.glob("*.py") if not p.is_dir()]
print(lista_archivos)
