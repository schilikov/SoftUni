numa = int(input())
numb = int(input())
operator = input()

if operator == '+':
    if (numa + numb) % 2 == 0:
        print(f"{numa} {operator} {numb} = {numa + numb} - even")
    else:
        print(f"{numa} {operator} {numb} = {numa + numb} - odd")

elif operator == '-':
    if (numa - numb) % 2 == 0:
        print(f"{numa} {operator} {numb} = {numa - numb} - even")
    else:
        print(f"{numa} {operator} {numb} = {numa - numb} - odd")

elif operator == '*':
    if (numa * numb) % 2 == 0:
        print(f"{numa} {operator} {numb} = {numa * numb} - even")
    else:
        print(f"{numa} {operator} {numb} = {numa * numb} - odd")

elif operator == '/':
    if numb == 0:
        print(f"Cannot devide {numa} by 0")
    else:
        print(f"{numa} / {numb} = {(numa / numb):.2f}")

elif operator == '%':
    if numb == 0:
        print(f"Cannot devide {numa} by 0")
    else:
        print(f"{numa} % {numb} = {numa % numb}")