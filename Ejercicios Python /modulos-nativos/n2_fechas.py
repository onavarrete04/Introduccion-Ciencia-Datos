import time
from datetime import datetime

fecha = datetime(2023, 1, 1)
print(fecha)

fecha2 = datetime(2023, 2, 1)

ahora = datetime.now()
print(fecha, ahora)

print(fecha.strftime("%Y-%m-%d"))

print(time.time())


fechaStr = datetime.strptime("2023/01/03", "%Y/%m/%d")

print(fechaStr)

print(ahora.strftime("%Y-%m-%d"))
