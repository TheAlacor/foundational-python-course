user = {
    'name': 'Ricardo',
    'age': 29,
    'greet': 'Hola Mundo',
    'numbers': [1, 2, 3]
}

# .copy()
print("Method: .copy()")
user_copy = user.copy()
user_copy['age'] = 20
print(user)
# print(user_copy)

# .pop()
print("Method: .pop()")
user.pop('age')
print(user)

# .popitem()
print("Method: .popitem()") #remove the last key from the dictionary
user.popitem()
print(user)

# .update()
print("Method: .update") # change or add new keys and values
user.update({'name': 'Fernando'})
user.update({'cats': 2})
print(user)

# .append()
print("Method: .append()") #add new values to the respective key
user['skills'] = user.get('skills', [])
user['skills'].append('Python')
user['skills'].append('Django')
print(user)