
class Flyer:
    def fly(self):
        print("I can fly")

    def do_something(self):
        print("FlyFly")


class Swimmer:
    def swim(self):
        print("I can swim")

    def do_something(self):
        print("SwimSwim")


class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")


donald = Duck()
donald.fly()
donald.swim()
donald.quack()
donald.do_something()

# MRO (Method Resolution Order)
print(Duck.__mro__)