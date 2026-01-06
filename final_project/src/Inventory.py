class Inventory:
    LIMIT = 5
    
    def __init__(self):
        self._items = []
        
    def _items_length(self) -> int:
        return len(self._items)
        
    def add_item(self, item):
        len = self._items_length()

        if len < self.LIMIT:
            self._items.append(item)
        else:
            print("Inventory full")
    
    def status(self):
        if len(self._items) > 1:
            status = "El inventario tiene " + str(len(self._items)) + " items, son:"
        else:
            status = "El inventario tiene " + str(len(self._items)) + " item, es:"
            
        for item in self._items:
            status += "\n\t"
            status += item.status()
            
        return status 

    
            
            