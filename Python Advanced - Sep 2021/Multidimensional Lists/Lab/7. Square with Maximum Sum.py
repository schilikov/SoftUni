# Find the biggest sum of 2x2 in the matrix and print it
n, m = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(n):
    sublist = [int(x) for x in input().split(", ")]
    matrix.append(sublist)

biggest_sum = 0

for r in range(n - 1):
    for c in range(m - 1):
        current_sum = matrix[r][c] + \
          matrix[r][c + 1] + \
          matrix[r + 1][c] + \
          matrix[r + 1][c + 1]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            position = (r, c)

row, col = position

print(matrix[row][col], matrix[row][col+1])
print(matrix[row+1][col], matrix[row+1][col+1])
print(biggest_sum)