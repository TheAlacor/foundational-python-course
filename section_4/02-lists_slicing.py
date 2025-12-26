
shopping_cart = ['T-shirts','trainers','socks','trousers']

# print(shopping_cart[2])
# print(shopping_cart[3])

# inicio / fin
new_list = shopping_cart[1:4]

new_list[0] = "shoes"

print(new_list) # create a new list
print(shopping_cart)

# copy a list
# new_cart = shopping_cart / esta manera guarda la direccion en memoria para que guarde solo los datos guardados usa [:]
new_cart = shopping_cart[:]
new_cart[0] ="shirts"
print(shopping_cart)
print(new_cart)