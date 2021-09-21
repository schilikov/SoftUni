type = input()
kolko = int(input())
budget = int(input())

if type == 'Roses':
    sum = kolko * 5
    if kolko > 80:
        sum -= sum * 0.1
elif type == 'Dahlias':
    sum = kolko * 3.8
    if kolko > 90:
        sum -= sum * 0.15
elif type == 'Tulips':
    sum = kolko * 2.8
    if kolko > 80:
        sum -= sum * 0.15
elif type == 'Narcissus':
    sum = kolko * 3
    if kolko < 120:
        sum += sum * 0.15
elif type == 'Gladiolus':
    sum = kolko * 2.5
    if kolko < 80:
        sum += sum * 0.2
else:
    print("We dont sell this type of flowers!")

if sum > budget:
    print(f"Not enough money, you need {(sum - budget):.2f} leva more.")
elif sum < budget:
    print(f"Hey, you have a great garden with {kolko} {type} and {(budget - sum):.2f} money left")