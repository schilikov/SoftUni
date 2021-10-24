tabs = int(input())
salary = float(input())
havesalary = True
for sites in range(tabs):
    site = input()
    if site == 'Facebook':
        salary -= 150
    elif site == 'Instagram':
        salary -= 100
    elif site == 'Reddit':
        salary -= 50
    if salary <= 0:
            print("You have lost your salary.")
            havesalary = False
            break
if salary > 0:
    print(f"Your remaining salary is {salary}")