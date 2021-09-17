# Store and print the unique chemical elements
n = int(input())
elements = set()

for _ in range(n):
    elements = elements.union(set(input().split()))

[print(el) for el in elements]