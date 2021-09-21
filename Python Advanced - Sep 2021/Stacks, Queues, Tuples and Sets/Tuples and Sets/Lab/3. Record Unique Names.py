# Print all the unique names
num = int(input())

names = set()

for _ in range(num):
    names.add(input())

[print(name) for name in names]