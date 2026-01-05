
from abc import ABC, abstractmethod

# abstract class


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("zzzz....")


animal = Animal()