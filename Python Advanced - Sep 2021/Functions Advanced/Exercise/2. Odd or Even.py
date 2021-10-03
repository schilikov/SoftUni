command = input()
numbers = [int(x) for x in input().split()]

parity = 0 if command == "Even" else 1
filtered_numbers = sum(filter(lambda x: x % 2 == parity, numbers))

print(filtered_numbers * len(numbers))