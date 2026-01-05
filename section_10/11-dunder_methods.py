
# dunder

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hello I am {self.name}"

    def __len__(self):
        return len(self.name)


persona = Person("Ricardo")
print(persona)
print(len(persona))