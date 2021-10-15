# A functions that receives some strings, concatenates them, and returns the result
def concatenate(*args):
    result = ""
    for x in args:
        result += x
    return result


concatenate(input())

# Test Codes
# print(concatenate("Soft", "Uni", "Is", "Great", "!"))
# print(concatenate("I", " ", "Love", " ", "Python"))
