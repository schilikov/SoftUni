import math
year = input()
holiday = int(input())
naselo = int(input())

holiday = holiday * 0.666
sofiaplay = (48 - naselo) * 0.75

if year == 'leap':
    print(f"{math.floor((holiday + sofiaplay + naselo) * 1.15)}")
elif year == 'normal':
    print(f"{math.floor(holiday + sofiaplay + naselo)}")