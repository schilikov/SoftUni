# Find the number of all 2x2 squares containing identical chars in a matrix
n, m = [int(x) for x in input().split()]

matrix = []

for _ in range(n):
    matrix.append([x for x in input().split()])

matches = 0

for a in range(n-1):
    for b in range(m-1):
        if matrix[a][b] == matrix[a][b+1] == matrix[a+1][b] == matrix[a+1][b+1]:
            matches += 1

print(matches)