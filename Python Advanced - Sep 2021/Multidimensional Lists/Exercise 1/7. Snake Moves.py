r, c = [int(x) for x in input().split()]
word = input()

matrix = []
index = 0

for row in range(r):
    matrix.append([None] * c)
    for col in range(c):
        if row % 2 == 0:
            matrix[row][col] = word[index]
        else:
            matrix[row][c - 1 - col] = word[index]
        index = (index + 1) % len(word)

for x in matrix:
    print(''.join([str(a) for a in x]))