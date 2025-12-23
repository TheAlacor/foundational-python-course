age = int(input("Introduce your age: "))

if age < 0:
    print("the age can't be negative")
elif age <= 12:
    print("you are a young boy/girl")
elif age <= 17:
    print("you are a teenager")
elif age <= 64:
    print("You are an adult")
else:  
    print("You are an older adult")