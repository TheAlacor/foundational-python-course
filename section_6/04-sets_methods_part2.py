
# methods

# .union() add all the data from both sets
print("Method: .union()")
print("set 1: ")
set1 = {1,2,3}
print(set1)
print("set 2: ")
set2 = {4,5,6}
print(set2)
print("union_set: ")
union_set = set1.union(set2)
print(union_set)

# .intersection() add all common data from both sets
print("Method: intersection()")
print("set 1: ")
set1 = {1,2,3,4,5,6}
print(set1)
print("set 2: ")
set2 = {3,4,5,6,7,8}
print(set2)
print("intersection_set: ")
intersection_set = set1.intersection(set2)
print(intersection_set)

# .difference() add all uncommon data from both sets.Also the data mustn't be from the second set set1.difference(set2) 
print("Method: difference()")
print("set 1: ")
set1 = {1,2,3,4,5,6}
print(set1)
print("set 2: ")
set2 = {3,4,5,6,7,8} # 7 and 8 are from set2, so only the uncommon data from set1 it shows
print(set2)
print("difference_set: ")
difference_set = set1.difference(set2)
print(difference_set)

