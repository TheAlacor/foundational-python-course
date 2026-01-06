from src.Item import Item

def main():
    item1 = Item("Espada de diamante", "Daño : 9 ; Durabilidad : 300")
    print(item1.status())
    
if __name__ == "__main__":
    main()