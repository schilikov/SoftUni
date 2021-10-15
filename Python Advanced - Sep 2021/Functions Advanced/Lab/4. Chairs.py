# Print all possible combinations with the given length of the given count
def combinations(names, count, current_names=[]):
    if len(current_names) == count:
        print(", ".join(current_names))
        return

    for i in range(len(names)):
        current_names.append(names[i])
        combinations(names[i+1:], count, current_names)
        current_names.pop()


given_names = input().split(", ")
given_count = int(input())
combinations(given_names, given_count)

# Test Inputs
# Peter, George, Amy
# 2
# Mariya, Emily, Tom, Bob
# 1