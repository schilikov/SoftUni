# We should edit the Stack using the commands and then reverse it
from collections import deque
count = int(input())
queue = deque()

for i in range(count):
    num = input().split()
    if num[0] == "1":
        queue.append(num[1])
    elif num[0] == "2" and len(queue) > 0:
        queue.pop()
    elif num[0] == "3" and len(queue) > 0:
        print(max(queue))
    elif num[0] == "4" and len(queue) > 0:
        print(min(queue))

nums_reversed = []

for _ in range(len(queue)):
    nums_reversed.append(queue.pop())

print(", ".join(nums_reversed))