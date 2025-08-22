products = [{"item":"Apple", "Price":55,"Quantity":35},
            {"item":"Mango", "Price":95,"Quantity":25}
            ]
# for data in products:
#     item = data["item"]
#     Price = data["Price"]
#     print(f"Item : {item}, Price: {Price}")



no = int(input("Number of key values to add ? "))
for _ in range(no):
    pp = {}
    key = input("Enter Key : ")
    value = input("Enter value : ")
    pp[key] = value

products.append(pp)

print("New List : ",products)