# We should reverse the numbers using Stack
nums = input().split(" ")
nums_second = []

for _ in range(len(nums)):
    nums_second.append(nums.pop())

print(" ".join(nums_second))

# Test Inputs

# 1 2 3 4 5
# 1