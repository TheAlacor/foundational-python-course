from src.Inventory import Inventory
from src.friendlyMob import FriendlyMob
import random

class Player:
    def __init__(self,name,health):
        self._name = name
        self._health = health
        self._inventory = Inventory()
        self._pets = []
        
    def health_bar(self) -> str:
        hearts = "❤️ "
        return hearts * self._health
        
    def pick_item(self,item):
        self._inventory.add_item(item)
    
    def tame(self,mob):
        if mob.is_tamed():
            print(mob._name + " is already tamed.")
          
        chance = random.choice([True,False])
        if chance:
            mob._tamed = True
            self._pets.append(mob)
            print(mob._name + "is now " + self._name + "'s pet !")
        else:
            print(mob._name + "still a wild mob")
            
    def pets_to_string(self):
        pets_to_string = ""
        for pet in self._pets:
            pets_to_string =f"\n\t{pet.status()}"
        
        return pets_to_string
            
    def status(self):       
        return f"{self._name} - health: {self.health_bar()} ({self._health})\n - Inventory: {self._inventory.status()} \n - Pets: {self.pets_to_string()} "