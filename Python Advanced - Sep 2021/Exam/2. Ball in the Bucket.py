def is_outside(size, row, col):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False


matrix = [[x for x in input().split()] for _ in range(6)]
throws = [[int(x) for x in input()[1:-1].split(", ")] for _ in range(3)]

points = 0
buckets_hit = []
for throw in throws:
    current_row, current_col = throw[0], throw[1]
    if is_outside(6, current_row, current_col) or matrix[current_row][current_col].isnumeric():
        continue
    if matrix[current_row][current_col] == "B" and ([current_row, current_col] not in buckets_hit):
        buckets_hit.append([current_row, current_col])
        sum_of_column = []
        for row in range(6):
            if matrix[row][current_col].isnumeric():
                sum_of_column.append(int(matrix[row][current_col]))
        points += sum(sum_of_column)

if points >= 300:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
elif  200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif  100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")

# Test Inputs

# 10 30 B 4 20 24
# 7 8 27 23 11 19
# 13 3 14 B 17 В
# 12 5 21 22 9 6
# B 26 1 28 29 2
# 25 B 16 15 B 18
# (1, 1)
# (20, 15)
# (4, 0)

# B 30 14 23 20 24
# 29 8 27 18 11 19
# 13 3 B B 17 6
# 28 5 21 22 9 B
# 10 B 26 12 B 2
# 25 1 16 15 7 4
# (0, 0)
# (2, 2)
# (2, 3)