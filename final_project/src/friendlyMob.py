from src.mob import Mob

class FriendlyMob(Mob):
    def __init__(self,name,health,tamed):
        super().__init__(name,health)
        self.tamed = tamed
    
    def status(self): 
        pet = "is a tamed mob." if self.tamed else "is a wild mob."      
        return f"{self._name} - health: {self.health_bar()} ({self._health}) - {pet}"    