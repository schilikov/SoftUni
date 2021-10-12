# Complete all fast food orders and if not - print the rest
from collections import deque

food_quantity = int(input())
queue_orders = deque([int(x) for x in input().split()])

print(max(queue_orders))

for i in range(len(queue_orders)):
    orders = queue_orders.popleft()
    if food_quantity >= orders:
        food_quantity -= orders
    else:
        queue_orders.appendleft(orders)
        break

if len(queue_orders) == 0:
    print("Orders complete")
else:
    print(f'Orders left:', ' '.join([str(orders) for orders in queue_orders]))