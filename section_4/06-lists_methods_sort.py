# methods;
letters = ["a","b","m","o","c","z","g","d","e"]
print(letters)
# sort()
print("Method: sort ")
letters.sort()
print(letters)

# sorted(): this is a function
print("function: sorted ")  # esto es igual que hacer:
new_letters = sorted(letters)
print(new_letters)

"""
new_letters = letters[:]  /list slicing or you can use also: method copy()
new_letters = letters.copy()
print(new_letters.sort())
"""
# reverse()
letters = ["a","b","m","o","c","z","g","d","e"]
print("Method: reverse ")
letters.reverse()
print(letters)


