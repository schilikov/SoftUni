position_mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}


def is_position_in_range(pos):
    if 1 <= pos <= 9:
        return True
    return False


def is_place_available(board, pos):
    row, col = get_row_col(pos)
    if not board[row][col] == " ":
        return False
    return True


pass


def get_row_col(pos):
    return position_mapper[pos]


def print_current_board_state(board):
    [print(f"| {' | '.join(el)} |") for el in board]


def is_board_full(board):
    is_full = True
    for row in board:
        if " " in row:
            is_full = False
    return is_full


def is_row_winner(board):
    for row in board:
        if row.count('X') == len(row) or row.count('O') == len(row):
            return True
    return False


def is_col_winner(board):
    is_found = False

    first = [board[0][0], board[1][0], board[2][0]]
    second = [board[0][1], board[1][1], board[2][1]]
    third = [board[0][2], board[1][2], board[2][2]]

    if first.count('X') == len(board) or first.count('O') == len(board):
        is_found = True
    elif second.count('X') == len(board) or second.count('O') == len(board):
        is_found = True
    elif third.count('X') == len(board) or third.count('O') == len(board):
        is_found = True
    return is_found


def is_primary_diagonal_winner(board):
    current_values = []
    for row in range(len(board)):
        current_values.append(board[row][row])
    if current_values.count("X") == len(board) or current_values.count("O") == len(board):
        return True
    return False


def is_second_diagonal_winner(board):
    current_values = []
    n = len(board)
    for i in range(len(board)):
        current_values.append(board[n-i-1][i])

    if current_values.count("X") == len(board) or current_values.count("O") == len(board):
        return True
    return False


def is_winner(board):
    if is_row_winner(board) or is_col_winner(board) \
            or is_primary_diagonal_winner(board) or is_second_diagonal_winner(board):
        return True
    return False


pass


def play(players, board, turns):
    current_turn_count = 1

    while True:
        current_player_name = turns[current_turn_count%2]
        position = int(input(f"{current_player_name} choose a free position: "))
        if is_position_in_range(position):
            if is_place_available(board, position):
                row, col = get_row_col(position)
                board[row][col] = players[current_player_name]
                print_current_board_state(board)
                if is_winner(board):
                    print(f"{current_player_name} wins!")
                    exit(0)
                if is_board_full(board):
                    print("Game over! No winner!")
                    exit(0)
        else:
            # Read new position for the same player
            pass

        current_turn_count += 1


pass


def print_initial_boar_positions():
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")


def create_empty_board():
    return [[" ", " ", " "] for _ in range(3)]


def start_game():
    player_1 = input("Player 1 name: ")
    player_2 = input("Player 2 name: ")
    player_1_sign = input(f"{player_1}, choose your sign (X or O): ").upper()
    while not player_1_sign in ["X", "O"]:
        player_1_sign = input(f"{player_1}, choose your sign (X or O): ").upper()
    player_2_sign = "O" if player_1_sign == "X" else "X"
    print(f"{player_1} starts first")
    print_initial_boar_positions()
    board = create_empty_board()
    players = {player_1: player_1_sign, player_2: player_2_sign}
    turns_mapper = {0: player_2, 1: player_1}
    play(players, board, turns_mapper)


start_game()