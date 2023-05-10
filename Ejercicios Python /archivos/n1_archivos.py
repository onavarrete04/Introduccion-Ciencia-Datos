from pathlib import Path
from time import ctime
archivo = Path("archivos/archivo_prueba.txt")
# archivo.exists() # para ver si existe
# archivo.rename() # renombrar
# archivo.unlink() # eliminar el archivo

archivo.stat()  # imrime la estadistica del archivo

print("acceso", ctime(archivo.stat().st_atime))
print("creación", ctime(archivo.stat().st_ctime))
print("modificación", ctime(archivo.stat().st_mtime))
