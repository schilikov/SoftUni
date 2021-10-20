from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
making_capacity = [int(x) for x in input().split(", ")]

total_pizzas_made = 0
orders = len(pizza_orders)

while True:
    if len(pizza_orders) == 0 or len(making_capacity) == 0 or orders == 0:
        break

    current_order = pizza_orders.popleft()
    current_employee = making_capacity.pop()

    if current_order > 10 or current_order <= 0:
        making_capacity.append(current_employee)
        continue

    if current_order <= current_employee:
        orders -= 1
        total_pizzas_made += current_order
    else:
        pizza_orders.appendleft(current_order - current_employee)
        total_pizzas_made += current_employee

if len(pizza_orders) == 0:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_made}")
    print(f"Employees: {', '.join([str(x) for x in making_capacity])}")

if len(making_capacity) == 0:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")

# Test Inputs

# 11, 6, 8, 1
# 3, 1, 9, 10, 5, 9, 1

# 10, 9, 8, 7, 5
# 5, 10, 9, 8, 7

# 12, -3, 14, 3, 2, 0
# 10, 15, 4, 6, 3, 1, 22, 1