days = int(input())
room = input()
sale = input()
nights = days - 1
price = 0

if room == 'a':
    price = nights * 18

if room == 'b':
    price = nights * 25
    if days < 10:
        price -= price * 0.3
    elif 10 <= days <= 15:
        price -= price * 0.35
    elif days > 15:
        price -= price * 0.5

if room == 'c':
    price = nights * 35
    if days < 10:
        price -= price * 0.1
    elif 10 <= days <= 15:
        price -= price * 0.15
    elif days > 15:
        price -= price * 0.2

if sale == 'Negative':
    off = 0.9
elif sale == 'Positive':
    off = 1.25

endsum = price * off

print(f"{endsum:.2f}")