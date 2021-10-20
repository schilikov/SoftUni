import math


def is_outside(size, r, c):
    if r >= size or c >= size or r < 0 or c < 0:
        return True
    return False

n = 7
player_one, player_two = input().split(", ")

matrix = [[str(x) for x in input().split()] for _ in range(n)]

turn = {
    1: player_one,
    0: player_two
}

points = {
    player_one: 501,
    player_two: 501
}

turns_count = 1

while True:
    row, col = [int(el) for el in input()[1:-1].split(", ")]

    if turns_count % 2 == 1:
        current_player = player_one
    else:
        current_player = player_two

    if is_outside(n, row, col):
        turns_count += 1
        continue
    else:
        current_hit = matrix[row][col]
        if current_hit.isdigit():
            points[current_player] -= int(current_hit)
        elif current_hit == "D":
            hit_sum = \
                (int(matrix[0][col]) +
                 int(matrix[row][n - 1]) +
                 int(matrix[n - 1][col]) +
                 int(matrix[row][0])) * 2
            points[current_player] -= hit_sum
        elif current_hit == "T":
            hit_sum = \
                (int(matrix[0][col]) +
                 int(matrix[row][n - 1]) +
                 int(matrix[n - 1][col]) +
                 int(matrix[row][0])) * 3
            points[current_player] -= hit_sum
        elif current_hit == "B":
            print(f"{current_player} won the game with {math.ceil(turns_count / 2)} throws!")
            exit(0)

    if points[player_one] <= 0 or points[player_two] <= 0:
        break

    turns_count += 1

print(f"{turn[turns_count % 2]} won the game with {math.ceil(turns_count / 2)} throws!")

# Test Codes

# Ivan, Peter
# 12 21 18 4 20 7 11
# 9 D D D D D 10
# 15 D T T T D 3
# 2 D T B T D 19
# 17 D T T T D 6
# 22 D D D D D 14
# 5 8 23 13 16 1 24
# (3, 3)

# George, Hristo
# 17 8 21 6 13 3 24
# 16 D D D D D 14
# 7 D T T T D 15
# 23 D T B T D 2
# 9 D T T T D 22
# 19 D D D D D 10
# 12 18 4 20 5 11 1
# (1, 0)
# (2, 3)
# (0, 0)
# (4, 2)
# (5, 1)
# (3, 1)
# (0, 0)
# (2, 3)