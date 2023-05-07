"""Herencia"""


class Animal:

    def commer(self):
        print("comiendo")


class Perro(Animal):
    def pasear(self):
        print("paseando")


class Chanchito(Perro):

    def programar(self):
        print("programando")
