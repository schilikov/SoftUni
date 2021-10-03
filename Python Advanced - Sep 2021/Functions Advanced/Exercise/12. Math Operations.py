from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)
    while numbers:
        kwargs["a"] += numbers.popleft()
        if not numbers:
            break

        kwargs["s"] -= numbers.popleft()
        if not numbers:
            break

        divide_number = numbers.popleft()
        if divide_number != 0:
            kwargs["d"] /= divide_number

        if not numbers:
            break

        kwargs["m"] *= numbers.popleft()

    return kwargs