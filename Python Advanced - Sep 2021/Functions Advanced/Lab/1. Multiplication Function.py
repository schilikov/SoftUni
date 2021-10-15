# Multiply all of the args and print the sum
def multiply(*args):
    sum = 1
    for x in args:
        sum *= x

    return sum

# Test Codes
# print(multiply(1, 4, 5))
# print(multiply(1, 4, 5))
# print(multiply(2, 0, 1000, 5000))