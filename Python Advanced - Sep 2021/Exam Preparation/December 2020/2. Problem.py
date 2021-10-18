def is_outside(field, row, col):
    if row < 0 or col < 0 or row >= field or col >= field:
        return True
    return False


def next_move(direction, r, c):
    if direction == "up":
        return r - 1, c
    if direction == "down":
        return r + 1, c
    if direction == "left":
        return r, c - 1
    return r, c + 1


word = [str(x) for x in input()]
size = int(input())

matrix = []
for _ in range(size):
    line = [str(x) for x in input()]
    matrix.append(line)

player_row, player_col = 0, 0
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "P":
            player_row, player_col = row, col

command_count = int(input())
for _ in range(command_count):
    command = input()

    next_row, next_col = next_move(command, player_row, player_col)

    if is_outside(size, next_row, next_col):
        if word:
            word.pop()
        continue

    if matrix[next_row][next_col].isalpha():
        word.append(matrix[next_row][next_col])

    matrix[player_row][player_col] = "-"
    matrix[next_row][next_col] = "P"
    player_row, player_col = next_row, next_col

print(''.join([str(x) for x in word]))
for x in matrix:
    print(''.join([str(el) for el in x]))