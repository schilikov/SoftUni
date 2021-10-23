from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

presents_made = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magic_levels:
    current_material = materials.pop()
    current_magic = magic_levels.popleft()
    current_sum = current_material + current_magic

    if current_sum < 100:
        if current_sum % 2 == 0:
            current_material *= 2
            current_magic *= 3
            current_sum = current_material + current_magic
        else:
            current_sum *= 2
    if current_sum > 499:
        current_material /= 2
        current_magic /= 2
        current_sum = current_material + current_magic
    if 100 <= current_sum <= 199:
        presents_made["Gemstone"] += 1
        continue
    elif 200 <= current_sum <= 299:
        presents_made["Porcelain Sculpture"] += 1
        continue
    elif 300 <= current_sum <= 399:
        presents_made["Gold"] += 1
        continue
    elif 400 <= current_sum <= 499:
        presents_made["Diamond Jewellery"] += 1
        continue
    else:
        continue

if (presents_made["Gemstone"] > 0 and  presents_made["Porcelain Sculpture"] > 0) or (presents_made["Gold"] > 0 and presents_made["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
    if materials:
        print(f"Materials left: {', '.join([str(x) for x in materials])}")
    if magic_levels:
        print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")
else:
    print("Aladdin does not have enough wedding presents.")
    if materials:
        print(f"Materials left: {', '.join([str(x) for x in materials])}")
    if magic_levels:
        print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

sorted_dict = sorted(presents_made.items(), key=lambda x: x[0])
for key, value in sorted_dict:
    if value > 0:
        print(f"{key}: {value}")

# Test Inputs

# 105 20 30 25
# 120 60 11 400 10 1

# 30 5 21 6 0 91
# 15 9 5 15 8

# 200
# 5 15 32 20 10 5