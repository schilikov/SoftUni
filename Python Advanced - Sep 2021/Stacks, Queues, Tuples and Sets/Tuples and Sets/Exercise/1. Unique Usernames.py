# Print the unique names only
num = int(input())
all_people = set()

for _ in range(num):
    all_people.add(input())

[print(p) for p in all_people]