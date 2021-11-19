from collections import deque


class dictionary_iter:
    def __init__(self, pack: dict):
        self.pack = pack
        self.counter = 0
        self.keys = deque(self.pack.keys())

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.keys) == 0:
            raise StopIteration

        key = self.keys.popleft()
        value = self.pack[key]
        return key, value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)