stock =  [] 

n = int(input("Enter no of products to add: "))
for i in range(n):
    product = input("Enter product name")
    price = int(input("Enter product price"))
    quantity = int(input("Enter product quantity"))

    if price > 50 or quantity > 10:
        discount = price * 0.5
        price -= discount
        print(f"Discount applied. New price: {price:.2f}")
    else:
        print("No discount for you")
    stock.append({"Product": product, "Price": round(price, 2), "Quantity": quantity})

print("Final Stock:")
for item in stock:
    print(item)