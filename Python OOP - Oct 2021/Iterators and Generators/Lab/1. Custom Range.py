class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        value = self.start
        self.start += 1
        return value


one_to_ten = CustomRange(1, 10)
for num in one_to_ten:
    print(num)