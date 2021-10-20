from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

bombs_count = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

datura, cherry, smoke_decoy = 40, 60, 120

success = False
while bomb_effects and bomb_casings:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()
    sum_of_bomb = current_effect + current_casing

    if sum_of_bomb == datura:
        bombs_count["Datura Bombs"] += 1
    elif sum_of_bomb == cherry:
        bombs_count["Cherry Bombs"] += 1
    elif sum_of_bomb == smoke_decoy:
        bombs_count["Smoke Decoy Bombs"] += 1
    else:
        bomb_effects.appendleft(current_effect)
        bomb_casings.append(current_casing - 5)

    num = 0
    for bomb in bombs_count.keys():
        if bombs_count[bomb] >= 3:
            num += 1

    if num == 3:
        success = True
        break
    else:
        num = 0

if success:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")

sorted_dict = sorted(bombs_count.items(), key=lambda x: x[0])

for key, value in sorted_dict:
    print(f"{key}: {value}")

# Test Inputs

# 5, 25, 25, 115
# 5, 15, 25, 35

# 30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
# 20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10