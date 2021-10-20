def get_magic_triangle(number):
    triangle = [[1], [1, 1]]
    for row in range(2, number):
        triangle.append([])
        triangle[-1].append(1)
        for col in range(1, row):
            triangle[-1].append(
                triangle[row - 1][col - 1] +
                triangle[row - 1][col]
            )
        triangle[-1].append(1)

    return triangle

# Test Code

# get_magic_triangle(5)