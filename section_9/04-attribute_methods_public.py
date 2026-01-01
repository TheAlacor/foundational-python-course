class Person:
    species = "Human"

    def __init__(self, name, age):
        self.name = name  # instance attributes
        self.age = age

    def work(self):
        return f"{self.name} he is working hard"

    def eat(self, food):
        if food.lower() == 'tacos':
            return "SUPERPOWERS"
        else:
            return "+Energy"


person1 = Person('Ricardo', 29)
print(person1.name)
print(person1.age)
print(person1.species)
print(person1.work())
print(person1.eat('tacos'))