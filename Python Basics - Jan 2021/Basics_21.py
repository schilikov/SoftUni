goal = 10000
stepsreached = 0

while stepsreached < goal:
    command = input()
    if command == 'going home':
        stepsbackhome = int(input())
        stepsreached += stepsbackhome
        break
    stepsreached += float(command)

if stepsreached >= goal:
    print(f"Goal reached! Good job! {abs(stepsreached - goal)} steps over the goal!")
if stepsreached < goal:
    print(f"{abs(goal - stepsreached)} more steps to reach goal.")