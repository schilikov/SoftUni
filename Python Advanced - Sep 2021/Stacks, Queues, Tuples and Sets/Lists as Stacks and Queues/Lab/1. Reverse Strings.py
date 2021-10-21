# We must reverse and move the given string from "word" to "result"
word = list(input())
result = []

while len(word) > 0:
    result.append(word.pop())

print(f"{''.join(result)}")

# Test Inputs

# I Love Python
# Stacks and Queues