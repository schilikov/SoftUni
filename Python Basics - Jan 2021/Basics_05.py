film = input()
redove = int(input())
koloni = int(input())

if film == 'premiere':
    print(f"{(12 * redove * koloni):.2f} leva.")
elif film == 'normal':
    print(f"{(7.5 * redove * koloni):.2f} leva.")
elif film == 'discount':
    print(f"{(5 * redove * koloni):.2f} leva.")