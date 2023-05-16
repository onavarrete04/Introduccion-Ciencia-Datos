url = "https://jsonplaceholder.typicode.com/users/2"


user = {
    "name": "chanchito feliz"
}
apikey = "12345"
headers = {
    "Autorization": f"Bearer {apikey}"
}

r_1 = requests.delete(url, timeout=10, headers=headers)
print(r_1.status_code)

# Es comun que las api tengan estas listas, pero eso
# debe verificarse con cada api por individual
