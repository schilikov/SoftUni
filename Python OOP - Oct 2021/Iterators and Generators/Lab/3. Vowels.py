class vowels:
    VOWELS = "aeiuyoAEIUYO"

    def __init__(self, text):
        self.text = text
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.text):
            if self.text[self.idx] in self.VOWELS:
                value = self.text[self.idx]
                self.idx += 1
                return value
            else:
                self.idx += 1

        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)