import string
import random

def password_generator(length):
    
    chars = string.ascii_letters + string.digits + string.punctuation
    password = []
    
    for item in range(length):
        index = random.choice(chars)
        password.append(index)
    
    return ''.join(password)

length = int(input("How many chars do you want in your password?\n "))
print("Your  secure password is:", password_generator(length))