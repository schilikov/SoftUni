# We should print all of the symbols between brackets
expression = input()
stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        start_index = stack.pop()
        print(expression[start_index: index+1])

# Test Inputs

# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
# (2 + 3) - (2 + 3)