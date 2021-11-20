def fibonacci():
    x, y = 0, 1

    yield x
    yield y

    while True:
        z = x + y
        yield z
        x, y = y, z


generator = fibonacci()
for i in range(5):
    print(next(generator))

