import itertools


def possible_permutations(nums):
    for permutation in itertools.permutations(nums):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]