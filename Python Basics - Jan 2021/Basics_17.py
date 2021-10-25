name = input()
sum = 0
fail = 0
klas = 1
while klas <= 12:
    grade = float(input())
    if grade < 4:
        fail += 1
        klas += 0
        sum += grade
        if fail == 2:
            print(f"{name} has been excluded at {klas}.")
            break
    if grade >= 4:
        klas += 1
        sum += grade
if fail < 2 and klas >= 12:
    print(f"{name} graduatet. Avarage grade: {(sum / 12 ):.2f}")