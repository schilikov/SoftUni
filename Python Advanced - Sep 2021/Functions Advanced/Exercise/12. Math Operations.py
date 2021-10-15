# Do some operations with the given arguments depending on the first letter of a kwargs
from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)
    while numbers:
        kwargs["a"] += numbers.popleft()
        if not numbers:
            break

        kwargs["s"] -= numbers.popleft()
        if not numbers:
            break

        divide_number = numbers.popleft()
        if divide_number != 0:
            kwargs["d"] /= divide_number

        if not numbers:
            break

        kwargs["m"] *= numbers.popleft()

    return kwargs

# Test Codes
# print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
# print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
# print(math_operations(6, a=0, s=0, d=0, m=0))