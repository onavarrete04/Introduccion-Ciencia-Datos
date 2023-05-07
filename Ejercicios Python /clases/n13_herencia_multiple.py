"""Herencia Multiple"""


class Animal:

    def commer(self):
        print("comiendo")

    def pasear(self):
        print("paseando al animal")


class Perro():
    def pasear(self):
        print("paseando al perro")


class Chanchito(Perro, Animal):

    def programar(self):
        print("programando")


# El problema que existe, es que hay dos metodos del mismo nombre
# estos los va a heredar chanchito, pero los va a eredar de izquierda a derecha,
# si el metodo de la izquierda Perro tiene pasear, se va a omitir el metodo pasear de Animal

# Esto es problematico porque si hay herencia multiple, cuenta en como se pasen los parametros
# porque asi es como los va a llamar el objeto chanchito cuando herede


objeto_chanchito = Chanchito()
objeto_chanchito.pasear()
