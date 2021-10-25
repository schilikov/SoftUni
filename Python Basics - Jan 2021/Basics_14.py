import sys
num = int(input())
maxnum = -sys.maxsize
minnum = sys.maxsize
for i in range(0, num):
    nums = int(input())

    if nums > maxnum:
        maxnum = nums
    if nums < minnum:
        minnum = nums

print(f"Max number:{maxnum}")
print(f"Min number:{minnum}")