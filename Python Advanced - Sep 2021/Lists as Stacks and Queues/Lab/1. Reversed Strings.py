word = list(input())
result = []

while len(word) > 0:
    result.append(word.pop())

print(f"{''.join(result)}")