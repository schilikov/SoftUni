# Print both diagonals in a square matrix and their sum
n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(", ")])

primary_diagonal = []
secondary_diagonal = []

for a in range(n):
    primary_diagonal.append(matrix[a][a])

for b in range(n):
    secondary_diagonal.append(matrix[b][n - b - 1])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")