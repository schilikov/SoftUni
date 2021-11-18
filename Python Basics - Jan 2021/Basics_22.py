sum = float(input())
sum = int(sum * 100)
coins = 0
coins += sum // 200
sum %= 200
coins += sum // 100
sum %= 100
coins += sum // 50
sum %= 50
coins += sum // 20
sum %= 20
coins += sum // 10
sum %= 10
coins += sum // 5
sum %= 5
coins += sum // 2
sum %= 2

if sum == 1:
    coins += 1
print(coins)