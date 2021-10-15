# Get all of the possible symbol combinations using recursion
def permute(index, values):
    if index >= len(values):
        print("".join(values))
        return
    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        permute(index + 1, values)
        values[i], values[index] = values[index], values[i]


permute(0, list(input()))

# Test Inputs
# abc
# 12