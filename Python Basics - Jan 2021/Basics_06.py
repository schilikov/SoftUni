grad = int(input())
time = input()

if time == 'morning':
    if 10 <= grad <= 18:
        outfit = 'sweatshirt'
        shoes = 'sneakers'
    elif 18 < grad <= 24:
        outfit = 'shirt'
        shoes = 'moccasins'
    elif grad >= 25:
        outfit = 'tshirt'
        shoes = 'sandals'

elif time == 'afternoon':
    if 10 <= grad <= 18:
        outfit = 'shirt'
        shoes = 'moccasins'
    elif 18 < grad <= 24:
        outfit = 'tshirt'
        shoes = 'sandals'
    elif grad >= 25:
        outfit = 'swim suit'
        shoes = 'barefoot'

elif time == 'evening':
    if 10 <= grad <= 18:
        outfit = 'shirt'
        shoes = 'moccasins'
    elif 18 < grad <= 24:
        outfit = 'shirt'
        shoes = 'moccasins'
    elif grad >= 25:
        outfit = 'shirt'
        shoes = 'moccasins'

print(f"It's {grad} degrees, get your {outfit} and {shoes}.")