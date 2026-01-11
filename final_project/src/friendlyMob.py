from src.mob import Mob

class FriendlyMob(Mob):
    def __init__(self,name,health):
        super().__init__(name,health)
        self._tamed = False
    
    def is_tamed(self):
        return self._tamed
    
    def status(self): 
        tame = "is a tamed mob." if self._tamed else "is a wild mob."      
        return f"{self._name} - health: {self.health_bar()} ({self._health}) - {tame}"    