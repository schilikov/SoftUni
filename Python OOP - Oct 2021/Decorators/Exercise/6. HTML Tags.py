def tags(letter):
    def decorator(func):
        def wrapper(*args):
            return f"<{letter}>" + func(*args) + f"</{letter}>"

        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
