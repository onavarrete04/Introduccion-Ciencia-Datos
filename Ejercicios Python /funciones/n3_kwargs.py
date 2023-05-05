"""kwargs"""


def get_product(**datos: dict):
    """Ejercicio kwargs"""
    print(datos["id"], datos["name"])


get_product(id="01",
            name="Iphone",
            desc="Esto es un Iphone")
