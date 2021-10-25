budget = int(input())
season = input()
ppl = int(input())

if season == 'Spring':
    sum = 3000
elif season == 'Summer' or season == 'Autumn':
    sum = 4200
elif season == 'Winter':
    sum = 2600

if ppl <= 6:
    sum -= sum * 0.1
elif 7 <= ppl <= 11:
    sum -= sum * 0.15
elif ppl >= 12:
    sum -= sum * 0.25

if ppl % 2 == 0:
    if season == 'Spring' or season == 'Summer' or season == 'Winter':
        sum -= sum * 0.05
    else:
        sum = sum

if budget >= sum:
    print(f"Yes! You have {(budget - sum):.2f} leva.")
elif budget < sum:
    print(f"Not enough money! You need {(sum - budget):.2f} leva.")