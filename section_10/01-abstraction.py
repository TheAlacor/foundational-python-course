
class CoffeMaker:
    def make_coffe(self):
        self.__boil_water()
        self.__mix()
        print("PIP PIP")
        print("Your coffee is ready")

    def __boil_water(self):
        print("Boiling water...")

    def __mix(self):
        print("Mixing coffee and water...")


coffe_maker = CoffeMaker()
coffe_maker.make_coffe()