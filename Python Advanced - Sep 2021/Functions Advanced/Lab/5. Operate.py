# A function that operates with different operators
from functools import reduce


def operate(operator, *args):
    return reduce(lambda x, y: eval(f"{x} {operator} {y}"), args)

# Test Codes
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))