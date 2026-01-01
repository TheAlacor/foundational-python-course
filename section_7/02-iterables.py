
numbers = [1, 2, 3, 4, 5]

# Iterables: Iterables, List, Dictionaries, Set, Tuples
# Iterador: An object that recall its position

# for number in numbers:
#     print(number)
iterator = iter(numbers)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

user = {
    'name': 'Ricardo',
    'age': 22,
    'can_swim': False
}

for key, value in user.items():
    print(key, value)