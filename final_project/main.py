from src.Item import Item
from src.Inventory import Inventory

def main():
    item1 = Item("Espada de Diamante", "Daño : 9 ; Durabilidad : 300")
    item2 = Item("Pico de Netherite", "Eficiencia : 5 ; Durabilidad : 800")
    item3 = Item("Pechera de Hierro", "Armadura : 6 ; Durabilidad : 300")
    item4 = Item("Manzana Dorada", "Regeneración : II ; Absorción : IV")
    item5 = Item("Arco de Llamas", "Poder : V ; Fuego : I ; Infinidad : 1")
    
    inventory = Inventory()
    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.add_item(item3)
    inventory.add_item(item4)
    inventory.add_item(item5)
    inventory.add_item(item1)
    
    print(inventory.status())
    
if __name__ == "__main__":
    main()