import math


def is_in_range(row, col):
    if row in range(7) and col in range(7):
        return True
    return False


def is_number(el):
    try:
        return int(el)
    except Exception:
        return False


n = 7

first_p, second_p = input().split(", ")
points = {first_p: 501, second_p: 501}

players_turns = {0: second_p, 1: first_p}
turns_count = 1

matrix = []
for _ in range(n):
    matrix.append(input().split())

while True:
    row, col = [int(el) for el in input()[1:-1].split(", ")]

    if is_in_range(row, col):
        number = is_number(matrix[row][col])
        if number:
            points[players_turns[turns_count % 2]] -= number

        current_points = sum([
            int(matrix[0][col]),
            int(matrix[-1][col]),
            int(matrix[row][0]),
            int(matrix[row][-1])
        ])

        if matrix[row][col] == "D":
            points[players_turns[turns_count % 2]] -= current_points * 2

        if matrix[row][col] == "T":
            points[players_turns[turns_count % 2]] -= current_points * 3

        if matrix[row][col] == "B":
            print(f"{players_turns[turns_count % 2]} won the game with {math.ceil(turns_count/2)} throws!")
            exit(0)

        if points[first_p] <= 0 or points[second_p] <= 0:
            break

    turns_count += 1

print(f"{players_turns[turns_count % 2]} won the game with {math.ceil(turns_count / 2)} throws!")