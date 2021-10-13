# Add to the matrix, print the sum of matrix and the matrix itself
n, m = [int(x) for x in input().split(", ")]


def read_matrix():
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)
    return matrix


matrix = read_matrix()
the_sum = 0

for row_index in range(n):
    row = matrix[row_index]
    for column_index in range(m):
        the_sum += row[column_index]

print(the_sum)
print(matrix)