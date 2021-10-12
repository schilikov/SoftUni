# Order the clothes from the box on the racks in the store
box = [int(x) for x in input().split()]
rack_capacity = int(input())

rack_count = 1
current_racks_weight = 0

for _ in range(len(box)):
    current_clothing = box.pop()
    if current_racks_weight + current_clothing > rack_capacity:
        rack_count += 1
        current_racks_weight = 0
    current_racks_weight += current_clothing

print(f"{rack_count}")