# Check which guests came to the pre-invitation party
num = int(input())
all_guests = set()

for _ in range(num):
    all_guests.add(input())

while True:
    command = input()
    if command == "END":
        break
    all_guests.remove(command)


def is_vip(guest):
    return guest[0].isdigit()


vip_guests = sorted([g for g in all_guests if is_vip(g)])
normal_guests = sorted([g for g in all_guests if not is_vip(g)])

print(len(all_guests))
[print(g) for g in vip_guests]
[print(g) for g in normal_guests]