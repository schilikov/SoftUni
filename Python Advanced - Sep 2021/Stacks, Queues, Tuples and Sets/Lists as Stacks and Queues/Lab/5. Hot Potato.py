# A game of hot potato
from collections import deque

children = deque(input().split())
count = int(input())

while len(children) > 1:
    children.rotate(-count)
    print(f"Removed {children.pop()}")

print(f"Last is {children.popleft()}")

# Test Inputs

# Tracy Emily Daniel
# 2

# George Peter Michael William Thomas
# 10

# George Peter Michael William Thomas
# 1