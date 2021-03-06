# We should print who got water, who should wait and how many liters are left
from collections import deque

liters = int(input())
name = input()
queue = deque()

while not name == "Start":
    queue.append(name)
    name = input()

command = input()

while not command == "End":
    if command.startswith("refill"):
        liters += int(command.split()[-1])
    else:
        liters_wanted = int(command)
        name = queue.popleft()
        if liters >= liters_wanted:
            liters -= liters_wanted
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    command = input()

print(f"{liters} liters left")

# Test Inputs

# 2
# Peter
# Amy
# Start
# 2
# refill 1
# 1
# End

# 10
# Peter
# George
# Amy
# Alice
# Start
# 2
# 3
# 3
# 3
# End