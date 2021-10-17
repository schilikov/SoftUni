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
game_status = None
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
    if coins_collected >= 100:
        game_status = True
        break

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

if game_status:
    print(f"You won! You've collected {floor(coins_collected)} coins.")
    print("Your path:")
    for step in path:
        print(step)