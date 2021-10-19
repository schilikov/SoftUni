board_size = int(input())
bombs_count = int(input())

board = [[int(x) for x in "0" * board_size] for row in range(board_size)]


def getting_bombs_positions():
    bomb_coordinates = []
    for _ in range(bombs_count):
        bomb = [int(x) for x in input()[1:-1].split(", ")]
        bomb_coordinates.append(bomb)

    return bomb_coordinates


bomb_list = getting_bombs_positions()


def printing_bombs_on_board(board):
    for idx in range(len(bomb_list)):
        row, col = bomb_list[idx][0], bomb_list[idx][1]
        board[row][col] = "*"

    return board


board_with_bombs = printing_bombs_on_board(board)

positions = [
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, +1),
    (0, +1),
    (+1, +1),
    (+1, 0),
    (+1, -1)
]


def is_inside(size, r, c):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


number = 0
for row in range(len(board)):
    for col in range(len(board[0])):
        current_row, current_col = row, col
        current_idx = board_with_bombs[current_row][current_col]

        if not current_idx == "*":
            for position in positions:
                pos_row, pos_col = position[0], position[1]
                pos_row_idx, pos_col_idx = pos_row + current_row, pos_col + current_col

                if is_inside(board_size, pos_row_idx, pos_col_idx):
                    for el in bomb_list:
                        bomb_row, bomb_col = el[0], el[1]
                        if pos_row_idx == bomb_row and pos_col_idx == bomb_col:
                            number += 1
                            break

            board_with_bombs[current_row][current_col] = number
            number = 0


def printing_matrix(board):
    for line in board:
        print(' '.join([str(x) for x in line]))


printing_matrix(board)


# Test Inputs

# 4
# 4
# (0, 3)
# (1, 1)
# (2, 2)
# (3, 0)

# 5
# 3
# (1, 1)
# (2, 4)
# (4, 1)