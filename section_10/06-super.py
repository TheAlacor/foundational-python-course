
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print(f"{self.name} make a noise")

    def info(self):
        print(f"My name is {self.name}, I have {self.age} years.")


class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def sound(self):
        super().sound()
        print(f"{self.name} says: Guau!")

    def info(self):
        super().info()
        print(f"My breed is {self.breed}")


class Cat(Animal):
    def sound(self):
        super().sound()
        print(f"{self.name} says: Miau!")


firulais = Dog('Firulais', 5, 'Labrador')
firulais.sound()
firulais.info()