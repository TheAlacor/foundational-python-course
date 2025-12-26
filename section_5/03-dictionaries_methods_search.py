
user = {
    "name": "Álvaro",
    "age": 18, 
    "greet": "hello world",
    "numbers": [1,2,3]  
}

print("Method: get()")
print(user.get("name")) # same as print(user["name"])

print("Method: in")
print("name" in user) # autoamtically create method .keys()
print("Álvaro" in user.keys()) # False, "Álvaro"/True when user.values()
print("name" in user.values()) # False, "name"/True when user.keys()

print(user.keys())
print(user.values())

print(user.items()) # show all elements