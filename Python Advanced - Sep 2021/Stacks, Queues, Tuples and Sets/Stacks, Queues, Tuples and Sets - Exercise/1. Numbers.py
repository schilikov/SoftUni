# Use the commands to edit the sets and then print them
line_one = set(input().split())
line_two = set(input().split())

n = int(input())
for _ in range(n):
    command = set(input().split())
    if "Add" in command:
        if "First" in command:
            command.remove("Add")
            command.remove("First")
            for num in command:
                line_one.add(num)

        elif "Second" in command:
            command.remove("Add")
            command.remove("Second")
            for num in command:
                line_two.add(num)

    elif "Remove" in command:
        if "First" in command:
            command.remove("Remove")
            command.remove("First")
            for num in command:
                if num in line_one:
                    line_one.remove(num)

        elif "Second" in command:
            command.remove("Remove")
            command.remove("Second")
            for num in command:
                if num in line_two:
                    line_two.remove(num)

    elif "Check" in command and "Subset" in command:
        if line_one.issubset(line_two) or line_two.issubset(line_one):
            print("True")
        else:
            print("False")

sorted_one, sorted_two = sorted(line_one), sorted(line_two)

print(", ".join(sorted_one))
print(", ".join(sorted_two))