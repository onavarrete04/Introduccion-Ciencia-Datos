
class Ave:

    def __init__(self):
        self.volador = "volador"

    def vuela(self):
        print("vuela ave")


class Pato(Ave):

    def __init__(self):
        super().__init__()
        self.nadar = "nadador"

    def vuela(self):
        # super.vuela()
        # # esto lo que hace es que no se omite, sino que se llama
        # obligatoriamente el de la clase padre, esto se puede hacer desde el init

        print("vuela pato")


pato = Pato()
pato.vuela()
print("---")

# En este caso se prioriza el metodo de la clase Pato
# Antes del metodo de la clase padre


print(pato.volador, pato.nadar)
