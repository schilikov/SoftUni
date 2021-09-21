# Print the nums that we can find in both of the sets
num_one, num_two = input().split()
num_one, num_two = int(num_one), int(num_two)
first_set, second_set = set(), set()

for _ in range(num_one):
    first_set.add(input())

for _ in range(num_two):
    second_set.add(input())

[print(num) for num in first_set.intersection(second_set)]