# Print the end result after calculation
from collections import deque

arithmetic_expressions = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}

characters = input().split()

numbers = deque()
for ch in characters:
    if ch in arithmetic_expressions:
        result = numbers.popleft()
        while numbers:
            number = numbers.popleft()
            result = arithmetic_expressions[ch](result, number)
        numbers.append(result)
    else:
        numbers.append(int(ch))

print(numbers.popleft())

# Test Inputs

# 6 3 - 2 1 * 5 /
# 2 2 - 1 *
# 10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *