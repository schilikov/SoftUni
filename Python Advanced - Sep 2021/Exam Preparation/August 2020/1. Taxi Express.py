from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]

total_time = 0

while customers and taxis:
    current_customer = customers.popleft()
    current_taxi = taxis.pop()

    if current_taxi >= current_customer:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")

if customers and not taxis:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")

# Test Inputs

# 4, 6, 8, 5, 1
# 1, 9, 15, 10, 6

# 10, 5, 8, 9
# 2, 4, 5, 8

# 2, 8, 4, 3, 11, 7
# 10, 15, 4, 6, 3, 10, 2, 1