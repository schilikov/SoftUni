# Create a matrix and print the sum of the primary diagonal
n = int(input())

matrix = []

for i in range(n):
    sublist = [int(x) for x in input().split()]
    matrix.append(sublist)

new_matrix = []

for a in range(len(matrix)):
        new_matrix.append(matrix[a][a])

print(sum(new_matrix))