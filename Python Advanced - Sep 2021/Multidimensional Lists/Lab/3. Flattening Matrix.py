# Add to the matrix, print the matrix flattered
n = int(input())

matrix = []
for _ in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

print([x for row in matrix for x in row])