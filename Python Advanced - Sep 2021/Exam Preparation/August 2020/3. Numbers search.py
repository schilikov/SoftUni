def numbers_searching(*args):
    numbers = [int(x) for x in args]

    double_nums = []
    whole_list = []

    minimum_num = min(numbers)
    maximum_num = max(numbers)
    for num in range(minimum_num, maximum_num + 1):
        if num not in numbers:
            whole_list.append(num)

    for _ in range(len(numbers)):
        current_num = numbers.pop()
        if current_num in numbers and current_num not in double_nums:
            double_nums.append(current_num)

    double_nums.sort()
    whole_list.append(double_nums)

    return whole_list


# Test Codes
# print(numbers_searching(1, 2, 4, 2, 5, 4))
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
# print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))