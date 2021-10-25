budget = float(input())
season = input()
destination = ""
pochivka = ""

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'Summer':
        pochivka = 'Camp'
        budget = budget * 0.3
    elif season == 'Winter':
        pochivka = 'Hotel'
        budget = budget * 0.7

elif budget <= 1000:
    destination = 'Balkans'
    if season == 'Summer':
        pochivka = 'Camp'
        budget = budget * 0.4
    elif season == 'Winter':
        pochivka = 'Hotel'
        budget = budget * 0.8

elif budget > 1000:
    destination = 'Europe'
    if season == 'Summer':
        pochivka = 'Hotel'
        budget = budget * 0.9
    elif season == 'Winter':
        pochivka = 'Hotel'
        budget = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{pochivka} - {budget:.2f}")