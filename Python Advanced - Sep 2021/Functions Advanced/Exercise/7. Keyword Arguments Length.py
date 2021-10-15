# A function that reads the length of the kwargs
def kwargs_length(**kwargs):
    return len(kwargs)

# Test Codes
# dictionary = {'name': 'Peter', 'age': 25}
# print(kwargs_length(**dictionary))
# dictionary = {}
# print(kwargs_length(**dictionary))
