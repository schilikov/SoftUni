city = str(input())
sold = float(input())

if city == 'Sofia':
    if 0 <= sold <= 500:
        print(f"{(sold * 0.05):.2f}")
    elif 500 < sold <=  1000:
        print(f"{(sold * 0.07):.2f}")
    elif 1000 < sold <= 10000:
        print(f"{(sold * 0.08):.2f}")
    elif sold > 10000:
        print(f"{(sold * 0.12):.2f}")
    else:
        print("Error")

elif city == 'Varna':
    if 0 <= sold <= 500:
        print(f"{(sold * 0.045):.2f}")
    elif 500 < sold <=  1000:
        print(f"{(sold * 0.075):.2f}")
    elif 1000 < sold <= 10000:
        print(f"{(sold * 0.1):.2f}")
    elif sold > 10000:
        print(f"{(sold * 0.13):.2f}")
    else:
        print("Error")

elif city == 'Plovdiv':
    if 0 <= sold <= 500:
        print(f"{(sold * 0.055):.2f}")
    elif 500 < sold <=  1000:
        print(f"{(sold * 0.08):.2f}")
    elif 1000 < sold <= 10000:
        print(f"{(sold * 0.12):.2f}")
    elif sold > 10000:
        print(f"{(sold * 0.145):.2f}")
    else:
        print("Error")

else:
    print("Error")