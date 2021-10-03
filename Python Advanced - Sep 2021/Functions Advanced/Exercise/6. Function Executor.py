def func_executor(*args):
    result = []
    for func, func_args in args:
        result.append(func(*func_args))
    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2