from src.Item import Item
from src.Inventory import Inventory
from src.friendlyMob import FriendlyMob
from src.player import Player

def main():
    # Testing Item class
    item1 = Item("Espada de Diamante", "Daño : 9 ; Durabilidad : 300")
    item2 = Item("Pico de Netherite", "Eficiencia : 5 ; Durabilidad : 800")
    item3 = Item("Pechera de Hierro", "Armadura : 6 ; Durabilidad : 300")
    item4 = Item("Manzana Dorada", "Regeneración : II ; Absorción : IV")
    item5 = Item("Arco de Llamas", "Poder : V ; Fuego : I ; Infinidad : 1")
    
    # Testing FriendlyMob class
    mob1 = FriendlyMob("Lobo",8)
    print(mob1.status())
    
    # Testing Player class
    player1 = Player("Steve",11)
    player1.pick_item(item1)
    player1.pick_item(item2)
    player1.pick_item(item3)
    player1.pick_item(item4)
    player1.pick_item(item5)
    player1.pick_item(item1)
    
    while mob1.is_tamed() != True:
        player1.tame(mob1)
        
    print(player1.status())
    
if __name__ == "__main__":
    main()