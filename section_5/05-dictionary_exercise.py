
students = {
    "Ana": [6,7,9],
    "Mark": [7,9,10],
    "Sarah": [8,8,9]
}

students['Mateo'] = students.get('Mateo', [])
students["Mateo"].append(9)
students["Mateo"].append(7)
students["Mateo"].append(8)
print(students)

name = "Ana"
if name in students:
    student_grades = students[name]
    total_grade = (student_grades[0]+student_grades[1]+student_grades[2]) / 3
    if total_grade >= 6:
        print(f"{name} passed with an average of:{total_grade:.2f}")
    else:
        print(f"{name} did not passed with an average of:{total_grade:.2f}")
else:
    print("Student is not registered")