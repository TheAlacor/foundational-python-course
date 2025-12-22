"""
name = input('User name: ')
email = input('User email (e.g.: alvaro@gmail.com): ')
year = int(input('Year of birth (e.g.: 2007): '))
password = input('Password (****): ')
age = (2050 - 2007)
str_age = str(age)
str_year = str(year)

print('-------------------')
print(name)
print(email)
print('Year: ' + str_year + ' and you will be ' + str_age + ' in 2050')
print(password)
"""

# course format

name = input('User name: ')
email = input('User email (e.g.: alvaro@gmail.com): ')
year = input('Year of birth (e.g.: 2007): ')
password = input('Password (****): ')

future_age = 2050 - int(year)
password_length = len(password)

card = f"""
    Name: {name}
    Email: {email}
    You will be {future_age} in 2050
    Your password is: {'*' * password_length}
"""

print(card)