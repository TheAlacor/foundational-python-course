from abc import ABC, abstractmethod

class Mob(ABC):

    def __init__(self, name, health):
        self._name = name
        self._health = health

    def health_bar(self) -> str:
        hearts = "❤️ "
        return hearts * self._health
    
    