# Print the sum divided by the length of the numbers depending on the give command
command = input()
numbers = [int(x) for x in input().split()]

parity = 0 if command == "Even" else 1
filtered_numbers = sum(filter(lambda x: x % 2 == parity, numbers))

print(filtered_numbers * len(numbers))

# Test Inputs
# Odd
# 1 3 5 34 7 9 12 11 13 10
# Even
# 1 3 5 7 9 13