
# .symmetric_difference() add all uncommon data from both sets
print("Method: symmetrical_difference()")
print("set 1: ")
set1 = {1,2,3,4,5,6}
print(set1)
print("set 2: ")
set2 = {3,4,5,6,7,8}
print(set2)
print("symmetrical_difference_set: ")
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)

# .issubset() show True/False if data from a set belong to other set like a subset
print("Method: issubset()")
print("set1: ")
set1 = {1,2}
print(set1)
print("set2: ")
set2 = {1,2,3,4,5}
print(set2)
print("issubset_set: ")
issubset_set = set1.issubset(set2)
print(issubset_set)

# .issuperset() show True/False if a set is master from a subset 
print("set1: ")
set1 = {1,2}
print(set1)
print("set2: ")
set2 = {1,2,3,4,5}
print(set2)
print("issubset_set: ")
issubset_set = set1.issubset(set2)
print(issubset_set)

