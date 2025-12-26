# Crearás un carrito de compras que haga las siguientes funcionalidades:
# Agregar producto
# Eliminar producto
# Mostrar la lista ordenada
# Buscar producto
# Contar productos del carrito
# Vaciar el carrito

print("Carrito de compras")
print("Opciones: ")
print("1. Agregar producto")
print("2. Eliminar producto")
print("3. Mostrar la lista ordenada")
print("4. Buscar producto")
print("5. Contar productos del carrito")
print("6. Vaciar el carrito")

shopping_cart = ["Laptop", "Vaso", "Cafe", "Audifonos"]
option = input("Elige una opción (1-6): ")

if option == "1":
    add = input("write the product you want to add: ")
    if add not in shopping_cart:
        shopping_cart.append(add)
        print(shopping_cart)
    else:
        print("This product is already in the list")
elif option == "2":
    remove = input("write the product you want to remove from the list: ")
    if remove in shopping_cart:
        shopping_cart.remove(remove)
        print(shopping_cart)
    else:
        print("This product is not from the list")
elif option == "3":
    print("lista ordenada alafabeticamente: ")
    shopping_cart.sort()
    print(shopping_cart)
elif option == "4":
    search = input("write the product you want to search: ")
    if search in shopping_cart:
        print(shopping_cart.index(search))
    else:
        print("product not found")
elif option == "5":
    print(len(shopping_cart))
elif option == "6":
    shopping_cart.clear()
    print("Clear function done:" + shopping_cart)
else:
    print("incorrect option") 