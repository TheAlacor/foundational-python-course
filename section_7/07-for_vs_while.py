# For: for iterables, we know when will it finish
# While: when we do not know when will it stop and we als oneed a condition
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)


item = 1
while item <= len(my_list):
    print(item)
    item = 1