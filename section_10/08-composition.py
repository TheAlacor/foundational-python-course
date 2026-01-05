
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


class Duck:

    def __init__(self):
        self.flyer = Flyer()
        self.swimmer = Swimmer()

    def quack(self):
        print("Quack!")

    def start_fly(self):
        self.flyer.fly()

    def start_swim(self):
        self.swimmer.swim()


donald = Duck()
donald.start_fly()
donald.start_swim()
donald.quack()
# donald.do_something()

# # MRO (Method Resolution Order)
# print(Duck.__mro__)