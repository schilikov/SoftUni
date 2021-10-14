# Create a matrix and do some modifications in it
def is_invalid_position(size, row, col):
    if 0 <= row < size and 0 <= col < size:
        return False
    return True


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == "END":
        break
    args = line.split()
    command = args[0]
    row, col, value = [int(x) for x in args[1:]]
    if is_invalid_position(size, row, col):
        print("Invalid coordinates")
        continue
    if command == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for row_el in matrix:
    print(' '.join([str(x) for x in row_el]))