"""
API REST

Aplications Programmin Interface
RE - representation
S - Stable
T - Transfer
"""

# GET -> Lee o lista
# POST -> Crea
# PUT / PATCH -> PUT - REEMPLAZAR - PATCH Actualizar
# DELETE -> Eliminar

import requests

# LECTURA - GET

# url = "https://jsonplaceholder.typicode.com/users"


# r = requests.get(url, timeout=10)

# print(
#     r.raise_for_status,
#     r.text,

# )

# r = r.json()

# for user in r:
#     print(user["name"])

# print("---")
# url = "https://jsonplaceholder.typicode.com/users/1/"


# r_1 = requests.get(url, timeout=10)

# print(r_1.json())

# # POST - ACTUALIZAR

# url = "https://jsonplaceholder.typicode.com/users"


# user = {
#     "name": "chanchito feliz"
# }

# r_1 = requests.post(url, timeout=10, data=user)
# print(r_1.status_code)

# # PUT- ACTUALIZAR

# url = "https://jsonplaceholder.typicode.com/users/2"


# user = {
#     "name": "chanchito feliz"
# }

# r_1 = requests.put(url, timeout=10, data=user)
# print(r_1.status_code)

#  DELETE - ELIMINAR

url = "https://jsonplaceholder.typicode.com/users/2"


user = {
    "name": "chanchito feliz"
}

r_1 = requests.delete(url, timeout=10)
print(r_1.status_code)
