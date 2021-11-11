class Calculator:

    @staticmethod
    def add(*args):
        return sum(x for x in args)

    @staticmethod
    def multiply(*args):
        result = 1
        for x in args:
            result *= x

        return result

    @staticmethod
    def divide(*args):
        first_num = args[0]
        for i in range(1, len(args)):
            first_num /= args[i]

        return first_num

    @staticmethod
    def subtract(*args):
        first_num = args[0]
        for i in range(1, len(args)):
            first_num -= args[i]

        return first_num


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))