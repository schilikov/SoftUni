# Using recursion, return the result of number ** power
def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power - 1)

# Test Codes
# print(recursive_power(2, 10))
# print(recursive_power(10, 100))