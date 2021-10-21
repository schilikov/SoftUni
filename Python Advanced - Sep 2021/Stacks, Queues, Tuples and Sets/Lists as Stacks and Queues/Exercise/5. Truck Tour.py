# From which petrol pump should we start so that we can fill up our tank in all of them
from collections import deque

petrol_pumps = int(input())
queue = deque()

for _ in range(petrol_pumps):
    pump = [int(x) for x in input().split()]
    queue.append(pump)

for attempt in range(petrol_pumps):
    petrol = 0
    completed = True
    for fuel, distance_to_next in queue:
        petrol += fuel
        if petrol < distance_to_next:
            completed = False
            break
        petrol -= distance_to_next
    if completed:
        print(attempt)
        break
    else:
        queue.append(queue.popleft())

# Test Inputs

# 3
# 1 5
# 10 3
# 3 4

# 5
# 22 5
# 14 10
# 52 7
# 21 12
# 36 9