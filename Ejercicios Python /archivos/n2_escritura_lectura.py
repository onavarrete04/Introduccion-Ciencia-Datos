from pathlib import Path

archivo = Path("archivos/archivo_prueba.txt")
texto = archivo.read_text("utf-8").split("\n")
print(texto)

texto.insert(0, "Hola, esto es una prueba")
archivo.write_text("\n".join(texto), "utf-8")
