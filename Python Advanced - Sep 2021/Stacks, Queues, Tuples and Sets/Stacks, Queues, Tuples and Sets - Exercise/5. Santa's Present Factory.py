# Craft presents
from collections import deque

boxes_with_materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

crafted_presents = {}

while boxes_with_materials and magic_levels:
    box = boxes_with_materials.pop()
    magic_value = magic_levels.popleft()
    result = box * magic_value

    if box == 0 and magic_value == 0:
        continue
    if box == 0:
        magic_levels.append(magic_value)
        continue
    if magic_value == 0:
        boxes_with_materials.append(box)
        continue

    if result < 0:
        boxes_with_materials.append(box + magic_value)
    elif result in presents:
        present = presents[result]

        if present in crafted_presents:
            crafted_presents[present] += 1
        else:
            crafted_presents[present] = 1
    else:
        boxes_with_materials.append(box + 15)

is_done = ('Doll' in crafted_presents and 'Wooden train' in crafted_presents) or \
          ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents)

if is_done:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if boxes_with_materials:
    print(f"Materials left: {', '.join(reversed([str(x) for x in boxes_with_materials]))}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

[print(f"{present}: {count}") for present, count in sorted(crafted_presents.items())]