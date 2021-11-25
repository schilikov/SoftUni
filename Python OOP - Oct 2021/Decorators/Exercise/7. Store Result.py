class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        with open("results_7.txt", "a") as file:
            func_result = self.func(*args)
            result = f"Function '{self.func.__name__}' was called. Result: {func_result}"
            file.write(result)
            file.write("\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
