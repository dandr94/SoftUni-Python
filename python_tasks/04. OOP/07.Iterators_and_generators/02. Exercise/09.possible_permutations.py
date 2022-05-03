from itertools import permutations

def possible_permutations(iter_list: list):
    for perm in permutations(iter_list):
        yield list(perm)


[print(n) for n in possible_permutations([1])]
[print(n) for n in possible_permutations([1, 2, 3])]

#  algorithms
