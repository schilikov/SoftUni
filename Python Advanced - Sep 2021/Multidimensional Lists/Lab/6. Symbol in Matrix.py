# Create a matrix and search for a specific symbol
n = int(input())

matrix = []

for i in range(n):
    sublist = input()
    matrix.append(sublist)

symbol = input()
row, column = None, None
is_found = False

for r in range(len(matrix)):
    if is_found:
        break
    for c in range(len(matrix[r])):
        if matrix[r][c] == symbol:
            row, column = r, c
            is_found = True
            break

if is_found:
    print((row, column))
else:
    print(f"{symbol} does not occur in the matrix")