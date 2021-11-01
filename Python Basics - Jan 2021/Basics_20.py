tripprice = float(input())
ownedmoney = float(input())
days = 0
spendingdays = 0

while ownedmoney < tripprice and spendingdays < 5:
    command = input()
    money = float(input())
    days += 1
    if command == 'save':
        ownedmoney += money
        spendingdays = 0
    elif command == 'spend':
        ownedmoney -= money
        spendingdays += 1
        if ownedmoney < 0:
            ownedmoney = 0

if spendingdays == 5:
    print('You cant save the money.')
    print(f"{days}")
if ownedmoney >= tripprice:
    print(f"You saved the money for {days} days.")