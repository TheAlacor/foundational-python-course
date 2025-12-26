
user = {
    "name": "Álvaro",
    "age": 18,
    "email": "correo@gmail.com"   # a list can't be a key(immutable - key)
    # a tuple can,example: coordinates from a country
}

user["name"] = "Sergio" # you can change the value from a key
user["age"] = 28
user["country"] = "Spain" # you can add new key with the respective value