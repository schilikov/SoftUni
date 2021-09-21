# Count how many times each number is in the tuple
nums = tuple([float(el) for el in input().split()])
nums_dict = {}

for num in nums:
    if num not in nums_dict:
        nums_dict[num] = 0
    nums_dict[num] += 1

sorted_nums_dict = sorted(nums_dict.items(), key=lambda x: x[0])
[print(f"{key} - {value} times") for key, value in sorted_nums_dict]