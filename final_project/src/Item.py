class Item:
    def __init__(self,name,desc):
        self.name = name
        self.desc = desc
    
    def status(self):
        return f"{self.name} - {self.desc}"     