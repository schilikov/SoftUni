from math import floor


def is_outside(size, r, c):
    if r < 0 or c < 0 or r >= size or c >= size:
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


valid_commands = [
    "up",
    "down",
    "left",
    "right"
]

size = int(input())
player_row, player_col = 0, 0

matrix = []
for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        el = matrix[row][col]
        if el == "P":
            player_row, player_col = row, col

coins_collected = 0
path = []

while True:
    command = input()

    if command not in valid_commands:
        continue

    next_row, next_col = next_move(command, player_row, player_col)

    if is_outside(size, next_row, next_col) or matrix[next_row][next_col] == "X":
        coins_collected = floor(coins_collected * 0.5)
        print(f"Game over! You've collected {coins_collected} coins.")
        print("Your path:")
        for step in path:
            print(step)
        exit(0)

    coins_collected += int(matrix[next_row][next_col])
    path.append([next_row, next_col])
    player_row, player_col = next_row, next_col

    if coins_collected >= 100:
        break


print(f"You won! You've collected {floor(coins_collected)} coins.")
print("Your path:")
for step in path:
    print(step)

# Test Inputs

# 5
# 1 X 7 9 11
# X 14 46 62 0
# 15 33 21 95 X
# P 14 3 4 18
# 9 20 33 X 0
# right
# right
# up
# up
# left
# down

# 8
# 13 18 9 7 24 41 52 11
# 54 21 19 X 6 4 75 6
# 76 5 7 1 76 27 2 37
# 92 3 25 37 52 X 56 72
# 15 X 1 45 45 X 7 63
# 1 63 P 2 X 43 5 1
# 48 19 35 20 100 27 42 80
# 73 88 78 33 37 52 X 22
# up
# left