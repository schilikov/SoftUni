def is_outside(row, col, size):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False


def get_next_position(direction, r, c):
    if direction == "up":
        return (r - 1, c)
    if direction == "down":
        return (r + 1, c)
    if direction == "left":
        return (r, c - 1)
    return (r, c + 1)


size = int(input())

matrix = []
alice_row, alice_col, bags_of_tea = 0, 0, 0

for _ in range(size):
    line = input().split()
    matrix.append([x for x in line])

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "A":
            alice_row, alice_col = r, c

matrix[alice_row][alice_col] = "*"

while True:
    command = input()
    alice_row, alice_col = get_next_position(command, alice_row, alice_col)
    if is_outside(alice_row, alice_col, size):
        break

    cell_value = matrix[alice_row][alice_col]
    matrix[alice_row][alice_col] = "*"
    if cell_value == "R":
        break

    if cell_value.isdigit():
        bags_of_tea += int(cell_value)
        if bags_of_tea >= 10:
            break

if bags_of_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for x in matrix:
    print(' '.join([str(a) for a in x]))