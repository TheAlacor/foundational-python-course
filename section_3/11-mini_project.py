# introduce if you know how to use Python/Django and how many year you have of experience(min:1):
"""
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
"""
"""
# chtgpt
options = ["y", "n"]

python_input = input("¿You know how to use Python? (y/n): ").lower()
django_input = input("¿You know how to use Django? (y/n): ").lower()
experience = int(input("How many years of experience do you have?: "))

# Validar opciones
if python_input not in options or django_input not in options:
    print("Incorrect option")
    exit()

python = python_input == "y"
django = django_input == "y"

# Evaluar experiencia
if experience > 3:
    result = "Op"
elif experience > 1:
    result = "Bu"
else:
    result = "Po"

# Evaluar candidato
if (python or django):
    if result == "Op":
        print("Candidato Óptimo")
    elif result == "Bu":
        print("Buen Candidato")
    else:
        print("Posible Candidato")
else:
    print("No cumple los requisitos")
"""
# curso
name = input("Nombre del candidato: ")
experience = int(input("Años de experiencia: "))
skills = input(
    "Ingrese sus habilidades separadas por comas (ej. Python, Laravel, Golang, Django, etc)").split(",")


evaluate_skills = "Python" in skills or "Django" in skills

result = ""
if evaluate_skills:
    if experience >= 3:
        result = "Candidato optimo"
    elif experience >= 1:
        result = "Buen candidato"
    else:
        result = "Posible candidato"
else:
    result = "No apto, se guardará CV para futuras ofertas"

print(f"El candidato {name} es: {result}")