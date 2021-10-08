month = input()
nights = int(input())

if month == 'May' or month == 'October':
    studio = 50 * nights
    apartment = 65 * nights
    if nights > 14:
        studio -= studio * 0.3
        apartment -= apartment * 0.1
    elif 7 < nights < 14:
        studio -= studio * 0.05
    else:
        studio = studio
        apartment = apartment

elif month == 'June' or month == 'September':
    studio = 75.2 * nights
    apartment = 68.7 * nights
    if nights > 14:
        studio -= studio * 0.2
        apartment -= apartment * 0.1
    else:
        studio = studio
        apartment = apartment

elif month == 'July' or month == 'August':
    studio = 76 * nights
    apartment = 77 * nights
    if nights > 14:
        apartment -= apartment * 0.1
    else:
        studio = studio
        apartment = apartment

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")