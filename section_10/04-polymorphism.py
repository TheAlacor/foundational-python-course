
class Animal:
    def make_sound(self):
        print("Animal noise")


class Dog(Animal):
    def make_sound(self):
        print("Woof Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow Meow!")


def make_noise(animal):
    if isinstance(animal, Animal):
        animal.make_sound()
    else:
        print("This is not an animal")


make_noise(Dog())
make_noise(Cat())
make_noise("Hello World")