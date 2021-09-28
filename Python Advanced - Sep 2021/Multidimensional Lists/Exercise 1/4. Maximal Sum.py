# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square that has maximal sum of its elements.
n, m = [int(x) for x in input().split()]

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

sum = 0
row = 0
col = 0

for a in range(n-2):
    for b in range(m-2):
        current_sum = matrix[a][b] + \
                      matrix[a][b+1] + \
                      matrix[a][b+2] + \
                      matrix[a+1][b] + \
                      matrix[a+1][b+1] + \
                      matrix[a+1][b+2] + \
                      matrix[a+2][b] + \
                      matrix[a+2][b+1] + \
                      matrix[a+2][b+2]
        if current_sum > sum:
            sum, row, col = current_sum, a, b

print(f"Sum = {sum}")
print(f"{matrix[row][col]} {matrix[row][col + 1]} {matrix[row][col + 2]}")
print(f"{matrix[row + 1][col]} {matrix[row + 1][col + 1]} {matrix[row + 1][col + 2]}")
print(f"{matrix[row + 2][col]} {matrix[row + 2][col + 1]} {matrix[row + 2][col + 2]}")