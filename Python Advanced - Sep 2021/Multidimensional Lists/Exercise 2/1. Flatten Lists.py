sublists = input().split("|")

result = []

for i in range(len(sublists) - 1, -1, -1):
    elements = sublists[i].split()
    result += elements

print(' '.join([str(x) for x in result]))