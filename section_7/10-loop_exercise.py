option = ""
shopping_cart = ["Laptop", "Glass", "Coffee", "Headphones"]

while option != "7":
    print()
    print("**********************")
    print("Shopping Cart")
    print("Options:")
    print("1. Add product")
    print("2. Remove product")
    print("3. Show sorted list")
    print("4. Search product")
    print("5. Count cart products")
    print("6. Empty the cart")
    print("7. Exit")
    print("**********************")

    option = input("Choose an option (1-7): ")

    if option == "1":
        product = input("Enter a product name: ")
        if product not in shopping_cart:
            shopping_cart.append(product)
            print("Product added")
        else:
            print("The product is already in your cart.")
    elif option == "2":
        product = input("Enter the product name to remove: ")
        if product in shopping_cart:
            shopping_cart.remove(product)
            print("Product removed")
        else:
            print("The product is not in the list")
    elif option == "3":
        if len(shopping_cart) > 0:
            print("Shopping list:")
            shopping_cart.sort()
            print(shopping_cart)
        else:
            print("The list is empty")
    elif option == "4":
        product = input("Enter a product name to search: ")
        if product in shopping_cart:
            print(f"{product} is in the list")
        else:
            print("Product not found")
    elif option == "5":
        print("Total products in your cart:", len(shopping_cart))
    elif option == "6":
        shopping_cart.clear()
        print("Cart emptied")
    else:
        print("Invalid option.")
else:
    print("Goodbye")