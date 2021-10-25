book = input()
searched = 0
command = input()
found = False
while command != 'No more books':
    if command == book:
        found = True
        print(f"You checked {searched} books and found it.")
        break

    searched += 1
    command = input()

if command == 'No more books':
    found = False
    print(f"Your book is not here and you checked {searched} books.")