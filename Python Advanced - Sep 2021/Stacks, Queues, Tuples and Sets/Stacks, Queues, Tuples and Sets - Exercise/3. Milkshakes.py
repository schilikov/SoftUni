# Make milkshakes (or don`t)
from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cup_of_milk = deque([int(x) for x in input().split(", ")])

milkshakes = 0

while chocolates and cup_of_milk and milkshakes < 5:
    chocolate = chocolates.pop()
    milk_cup = cup_of_milk.popleft()

    if chocolate <= 0 and milk_cup <= 0:
        continue
    if chocolate <= 0:
        cup_of_milk.appendleft(milk_cup)
        continue
    if milk_cup <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk_cup:
        milkshakes += 1
    else:
        cup_of_milk.append(milk_cup)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if cup_of_milk:
    print(f"Milk: {', '.join([str(x) for x in cup_of_milk])}")
else:
    print("Milk: empty")

# Test Inputs

# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55

# -10, -2, -30, 10
# -5

# 2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6