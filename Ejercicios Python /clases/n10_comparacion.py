"""Comparar dos objetos"""


class Coordenadas:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def __eq__(self, otro):
        return self.lat == otro.lat and self.long == otro.long

    def __ne__(self, otro):
        return self.lat != otro.lat and self.long != otro.long

    def __lt__(self, otro):
        return self.lat + self.long < otro.lat + otro.long


coords = Coordenadas(41, 27)
coords2 = Coordenadas(42, 27)


print(coords, coords2)
print(coords == coords2)  # igualdad qe
print(coords != coords2)  # diferencia ne
print(coords < coords2)  # mayor que lt

# esto muestra si son iguales por dentro con
# el metodo magico __eq__ pero normalmente mostraría
# es la posicion del objeto en la ram
