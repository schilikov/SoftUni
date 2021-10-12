# We should edit the Stack using the commands and then reverse it
from collections import deque
count = int(input())
stack = []

for i in range(count):
    num = input().split()
    if num[0] == "1":
        stack.append(num[1])
    elif num[0] == "2" and len(stack) > 0:
        stack.pop()
    elif num[0] == "3" and len(stack) > 0:
        print(max(stack))
    elif num[0] == "4" and len(stack) > 0:
        print(min(stack))

nums_reversed = []

for _ in range(len(stack)):
    nums_reversed.append(stack.pop())

print(", ".join(nums_reversed))