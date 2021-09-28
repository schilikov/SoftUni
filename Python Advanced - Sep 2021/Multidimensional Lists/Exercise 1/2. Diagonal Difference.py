# Print the absolute value of the sum of the both diagonals
n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

primary_diagonal = []
secondary_diagonal = []

for a in range(n):
    primary_diagonal.append(matrix[a][a])

for b in range(n):
    secondary_diagonal.append(matrix[b][n - b - 1])

print(f"{abs(sum(primary_diagonal) - sum(secondary_diagonal))}")