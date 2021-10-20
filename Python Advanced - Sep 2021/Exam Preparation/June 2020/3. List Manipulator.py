def list_manipulator(nums, command, position, *args):
    nums = nums
    new_list = []
    if command == "add" and position == "beginning":
        for i in args:
            new_list.append(i)
        for x in nums:
            new_list.append(x)
        return new_list
    elif command == "add" and position == "end":
        for i in args:
            nums.append(i)
        return nums
    elif command == "remove" and position == "beginning":
        if args:
            r = args[0]
            nums = nums[r:]
        else:
            nums = nums[1:]
        return nums
    elif command == "remove" and position == "end":
        if args:
            for _ in range(args[0]):
                nums.pop()
        else:
            nums.pop()
        return nums


# Test Codes

# print(list_manipulator([1,2,3], "remove", "end"))
# print(list_manipulator([1,2,3], "remove", "beginning"))
# print(list_manipulator([1,2,3], "add", "beginning", 20))
# print(list_manipulator([1,2,3], "add", "end", 30))
# print(list_manipulator([1,2,3], "remove", "end", 2))
# print(list_manipulator([1,2,3], "remove", "beginning", 2))
# print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))