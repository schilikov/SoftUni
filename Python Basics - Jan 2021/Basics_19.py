bad = int(input())
failedtasks = 0
gradesum = 0
tasknum = 0
lasttask = ''
failed = True
while failedtasks < bad:
    task = input()
    if task == 'Enough':
        failed = False
        break
    grade = int(input())
    if 2 <= grade <= 4:
        failedtasks += 1
    gradesum += grade
    tasknum += 1
    lasttask = task
    if grade > 6 or grade < 2:
        print(f"Invalid grade! Run the code again!")
if failed:
    print(f"You need a break, {failedtasks} poor grades.")
else:
    print(f"Average score: {(gradesum/tasknum):.2f}")
    print(f"Number of problems: {tasknum}")
    print(f"Last problem: {lasttask}")