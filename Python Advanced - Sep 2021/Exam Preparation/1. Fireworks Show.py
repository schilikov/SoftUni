from collections import deque

firework_effects = deque([int(x) for x in input(). split(", ")])
explosive_power = [int(x) for x in input(). split(", ")]

fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

success = None

while True:
    if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
        success = True
        break
    if len(firework_effects) <= 0 or len(explosive_power) <= 0:
        success = False
        break

    current_firework = firework_effects.popleft()
    current_explosive = explosive_power.pop()

    if current_explosive <= 0 and current_firework <= 0:
        continue
    if current_explosive <= 0:
        firework_effects.appendleft(current_firework)
        continue
    if current_firework <= 0:
        explosive_power.append(current_explosive)
        continue

    sum_of_both = current_firework + current_explosive

    if sum_of_both % 3 == 0 and sum_of_both % 5 != 0:
        fireworks["Palm Fireworks"] += 1
        continue
    if sum_of_both % 5 == 0 and sum_of_both % 3 != 0:
        fireworks["Willow Fireworks"] += 1
        continue
    if sum_of_both % 3 == 0 and sum_of_both % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
        continue

    firework_effects.append(current_firework - 1)
    explosive_power.append(current_explosive)

if success:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

for firework in fireworks:
    print(f"{firework}: {fireworks[firework]}")