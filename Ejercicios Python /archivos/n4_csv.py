import csv
import os

# escribir

# with open("archivos/archivo.csv", "w") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(("twit_id", "user_id", "text"))
#     writer.writerow(("1000", "1", "Este es un twit"))
#     writer.writerow(("1000", "2", "Este es un twit"))


# leer

# with open("archivos/archivo.csv") as archivo:
#     reader = csv.reader(archivo)
#     for linea in archivo:
#         print(linea)

# actualizar csv

with open("archivos/archivo.csv") as r, open("archivos/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)

    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000, 1, "Texto modificado"])
        else:
            writer.writerow(linea)
    os.remove("archivos/archivo.csv")
    os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")
