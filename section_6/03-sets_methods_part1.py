# sets

# methods
# .add()
print("Method: .add()")
my_set = {1,2,3}
my_set.add(6)
my_set.add(3) # add ignored because of the duplicate number 3
print(my_set)

# .remove() if number does not exist shows an error
print("Method: .remove()")
my_set = {1,2,3}
my_set.remove(3)
print(my_set)

# .discar() same as remove() but does not show an error if number not exist
print("Method: .discard()")
my_set= {1,2,3}
my_set.discard(3)
my_set.discard(4)
print(my_set)

# .pop() remove a ramdon number from the set
print("Method: .pop()")
my_set= {1,2,3}
print(my_set.pop())
print(my_set)
