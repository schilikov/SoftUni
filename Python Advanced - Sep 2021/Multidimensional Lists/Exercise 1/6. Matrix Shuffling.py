# Create a matrix and then swap some strings on specific indexes
def is_valid(row_r, col_c, row, col):
    if row_r >= row or col_c >= col or row_r < 0 or col_c < 0:
        return False
    return True


row, col = [int(x) for x in input().split()]

matrix = []

for a in range(row):
    matrix.append([str(x) for x in input().split()])

while True:
    line = input()
    if line == "END":
        break
    args = line.split()
    if args[0] != "swap" or len(args) != 5:
        print("Invalid input!")
        continue
    row1, col1, row2, col2 = [int(x) for x in args[1:]]
    if not is_valid(row1, col1, row, col) or not is_valid(row2, col2, row, col):
        print("Invalid input!")
        continue
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for i in matrix:
        print(' '.join([str(x) for x in i]))