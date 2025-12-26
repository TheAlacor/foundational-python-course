"""
# and(all values are true)
print(True and True) # true
print(True and False) # false
print(False and True) # false
print(False and False) # false

# or(atleast one value must be true)
print(True or True) # true
print(True or False) # true
print(False or True) # true
print(False or False) # false

# not(negative)
print(not True) # false
print(not False) # true
"""

# and
age = 25
licensed = True

if age >= 18 and licensed:
    print("You can drive")

# or
is_student = True
membership = False

if is_student or membership:
    print("you get a special discount")

# not
is_admin = False

if not is_admin:
    print("access denied")

    
    