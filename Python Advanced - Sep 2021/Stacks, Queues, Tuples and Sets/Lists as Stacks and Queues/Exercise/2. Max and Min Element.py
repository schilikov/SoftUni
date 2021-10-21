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

# Test Inputs

# 9
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 3
# 1 91
# 4

# 10
# 2
# 1 47
# 1 66
# 1 32
# 4
# 3
# 1 25
# 1 16
# 1 8
# 4