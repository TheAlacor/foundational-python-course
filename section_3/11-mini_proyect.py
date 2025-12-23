# introduce if you know how to use Python/Django and how many year you have of experience(min:1):

option = ["y,n,Y,N"]

result = ["Op,Bu,Po"]

python = input("¿You know how to use Python?(y/n) ")
django = input("¿You know how to use  Django? ")
experience = int(input("How many (year) have of experience(ej:1): "))
# or

if python not in option:
    print("Incorrect option")
elif python.lower == "y" in option:
    python = True
elif python.lower == "n" in option:
    python = False
elif django not in option:
    print("Incorrect option")
elif django.lower == "y" in option:
    django = True
elif django.lower == "n" in option:
    django = False
elif experience > 3:
    result = "Op"
elif experience > 1:
    result = "Bu"
elif experience <= 1 or experience < 0:
    result = "Po"
elif (python == True or django == True) and result == "Op":
    print("Candidato Optimo")
elif (python == True or django == True) and result == "Bu":
    print("Buen Candidato")
elif (python == True or django == True) and result == "Po":
    print("Posible")
elif (python == False or django == False):
    print("Candidato Optimo")