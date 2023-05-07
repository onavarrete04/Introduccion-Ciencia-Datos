class Lista(list):
    def prepend(self, item):
        self.insert(0, item)


lista = Lista([1, 2, 3, 4])

lista.append(5)
print(lista.prepend(0))

# se creo la forma de guardar datos en la posición inicial de 0
# esto puede hacerse con cualquier cosa
