def expression(nums, current_sum=0, current_expression=""):
    if not nums:
        print(f"{current_expression}={current_sum}")
        return
    expression(nums[1:], current_sum+nums[0], f"{current_expression}+{nums[0]}")
    expression(nums[1:], current_sum-nums[0], f"{current_expression}-{nums[0]}")


nums = [int(el) for el in input().split(", ")]
expression(nums)