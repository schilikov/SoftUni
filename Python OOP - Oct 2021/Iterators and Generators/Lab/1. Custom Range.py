class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current_number = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number > self.end:
            raise StopIteration

        value = self.current_number
        self.current_number += 1
        return value


one_to_ten = CustomRange(1, 10)
for num in one_to_ten:
    print(num)