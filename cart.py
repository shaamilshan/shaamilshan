cart = ["Shirt","Jean","Top","Kurta","Saree"]
print(cart)
print(cart[0])
print(cart[1:3])
cart.append("T-Shirts")
print(cart)

if "Jean" in cart:
    print("Jean is in the cart")
else:
    print("Item not in Cart")

item = input("Enter the item to be added in cart : ")
if item in cart:
    print("Item already exist")
else:
    cart.append(item)

print(cart)

rem = input("Enter the item to be removed from cart : ")
if rem in cart:
    cart.remove(rem)
    print(f"{item} removed")
else:
    print("Item not found")

print(cart)

while(1):
    print("\n1) Add 2) View 3) Exit")
    choice = input("Enter choice : ")
    if choice == "1":
        ad=input("Enter item to add : ")
        cart.append(ad)
        print("Added")
    elif choice == "2":
        print(cart)
    elif choice == "3":
        print("exiting...")
        break
    else:
        print("Invalid input")
