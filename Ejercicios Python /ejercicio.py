def calcularArray(lista: list):
    mayor_num = lista[0]
    if len(lista) == 0:
        return None

    elif len(lista) == 1:
        return lista[0]

    else:

        for i in range(len(lista)):
            if lista[i] > mayor_num:
                mayor_num = lista[i]

    print(mayor_num)


calcularArray([3, 1, 5, 2])
