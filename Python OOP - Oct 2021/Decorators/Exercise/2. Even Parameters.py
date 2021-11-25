def even_parameters(func):
    def wrapper(*args):
        evens = [x for x in args if x % 2 == 0]
        result = func(args)
        if len(evens) == len(args):
            return result

        return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
