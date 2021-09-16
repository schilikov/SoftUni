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