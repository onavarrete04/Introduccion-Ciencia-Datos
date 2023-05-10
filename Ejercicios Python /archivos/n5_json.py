"""Json """
import json
from pathlib import Path

# escribir json

# productos = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"}
# ]


# data = json.dumps(productos)
# print(data)

# Path("archivos/procutos.json").write_text(data)

# leer

data = Path("archivos/productos.json").read_text(encoding="utf-8")

leer_productos = json.loads(data)
print(leer_productos)

# modificar

leer_productos[0]["name"] = "Chanchito Feliz"
data = Path("archivos/productos.json").write_text(json.dumps(leer_productos))
