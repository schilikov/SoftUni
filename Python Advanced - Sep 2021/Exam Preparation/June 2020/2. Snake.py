def is_inside(size, r, c):
    if 0 <= r < size and 0 <= c < size:
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


n = int(input())
board = [[str(x) for x in input()] for _ in range(n)]

snake_row, snake_col = 0, 0
for row in range(n):
    for col in range(n):
        if board[row][col] == "S":
            snake_row, snake_col = row, col
            break

food_eaten = 0
while food_eaten < 10:
    command = input()
    next_row, next_col = next_move(command, snake_row, snake_col)
    board[snake_row][snake_col] = "."

    if not is_inside(n, next_row, next_col):
        print("Game over!")
        print(f"Food eaten: {food_eaten}")
        for line in board:
            print(f"{''.join([str(x) for x in line])}")
        exit(0)

    if board[next_row][next_col] == "*":
        food_eaten += 1

    if board[next_row][next_col] == "B":
        lair = []
        for row in range(n):
            for col in range(n):
                if board[row][col] == "B":
                    if row != next_row and col != next_col:
                        lair.append([row, col])

        lair_row, lair_col = lair[0]
        board[snake_row][snake_col] = "."
        board[next_row][next_col] = "."
        board[lair_row][lair_col] = "S"
        snake_row, snake_col = lair_row, lair_col
        continue

    board[next_row][next_col] = "S"
    snake_row, snake_col = next_row, next_col

print("You won! You fed the snake.")
print(f"Food eaten: {food_eaten}")
for line in board:
    print(f"{''.join([str(x) for x in line])}")

# Test Inputs

# 6
# -----S
# ----B-
# ------
# ------
# --B---
# --*---
# left
# down
# down
# down
# left

# 7
# --***S-
# --*----
# --***--
# ---**--
# ---*---
# ---*---
# ---*---
# left
# left
# left
# down
# down
# right
# right
# down
# left
# down