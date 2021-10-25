import math
fruit = str(input())
day = str(input())
how_much = float(input())

if day == 'Mo' or day == 'Tu' or day == "W" or day == "Th" or day == "F":
    if fruit == 'banana':
        price = 2.5
    elif fruit == 'apple':
        price = 1.2
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.7
    elif fruit == 'pineapple':
        price = 5.5
    elif fruit == 'grapes':
        price = 3.85
    else:
        print("Error")

elif day == 'Sa' or day == 'Su':
    if fruit == 'banana':
        price = 2.7
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.9
    elif fruit == 'grapefruit':
        price = 1.6
    elif fruit == 'kiwi':
        price = 3.0
    elif fruit == 'pineapple':
        price = 5.6
    elif fruit == 'grapes':
        price = 4.2
    else:
        print("Error")

else:
    print("Error")

endsum = price * how_much

print(round(endsum, 2))