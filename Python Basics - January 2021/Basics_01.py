product = str(input())
city = str(input())
how_much = float(input())

if city == "Sofia":
    if product == "coffee":
        price = 0.5
    elif product == "water":
        price = 0.8
    elif product == "beer":
        price = 1.2
    elif product == "sweets":
        price = 1.45
    elif product == "peanuts":
        price = 1.6
    else:
        print("Product out of stock!")

elif city == "Plovdiv":
    if product == "coffee":
        price = 0.4
    elif product == "water":
        price = 0.7
    elif product == "beer":
        price = 1.15
    elif product == "sweets":
        price = 1.3
    elif product == "peanuts":
        price = 1.5
    else:
        print("Product out of stock!")

elif city == "Varna":
    if product == "coffee":
        price = 0.45
    elif product == "water":
        price = 0.7
    elif product == "beer":
        price = 1.1
    elif product == "sweets":
        price = 1.35
    elif product == "peanuts":
        price = 1.55
    else:
        print("Product out of stock!")

else:
    print("We do not sell in your city!")

print(f"Total:{(how_much * price):.2f}")