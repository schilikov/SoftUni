board = [[el for el in input().split()] for _ in range(8)]


def found_the_king(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "K":
                return row, col


def is_inside(size, r, c):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def searching_with_deltas(board, king, deltas):
    row_count, col_count = len(board), len(board[0])
    delta_row, delta_col = deltas
    row_index, col_index = king

    while True:
        if not is_inside(8, row_index, col_index):
            return None
        if board[row_index][col_index] == "Q":
            return [row_index, col_index]

        row_index += delta_row
        col_index += delta_col


def capturing_queens(board, king):
    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, +1),
        (+1, +1),
        (+1, 0),
        (+1, -1)
    ]
    queens = [searching_with_deltas(board, king, delta) for delta in deltas]

    return [queen for queen in queens if queen]


def print_result(queens):
    if queens:
        for queen in queens:
            print(queen)
    else:
        print("The king is safe!")


king = found_the_king(board)
queens = capturing_queens(board, king)
print_result(queens)