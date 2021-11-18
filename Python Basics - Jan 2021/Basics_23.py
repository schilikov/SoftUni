dulgo = int(input())
shiroko = int(input())
pieces = int(dulgo * shiroko)
takenpieces = 0

while takenpieces < pieces:
    command = input()
    if command == 'stop':
        print(f"{abs(pieces - takenpieces)} pieces are left.")
        break
    takenpieces += int(command)

if takenpieces > pieces:
    print(f"No more cake let! You need {abs(takenpieces - pieces)} pieces more.")
if takenpieces == pieces:
    print(f"No more cake let!")