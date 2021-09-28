n, m = [int(x) for x in input().split()]

for a in range(n):
    for b in range(m):
        print(f"{chr(97 + a)}{chr(97 + a + b)}{chr(97 + a)}", end=" ")
    print()