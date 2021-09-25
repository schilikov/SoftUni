# Add to the matrix and print all column sums
n, m = [int(x) for x in input().split(", ")]

def read_matrix():
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


matrix = read_matrix()
column_sums = [0] * m

for a in range(n):
    for b in range(m):
        value = matrix[a][b]
        column_sums[b] += value

[print(x) for x in column_sums]


