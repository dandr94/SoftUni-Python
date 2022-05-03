import sys
from collections import deque


def best_list_pureness(list_of_numbers, k):
    my_list = deque(list_of_numbers)

    final = -sys.maxsize
    best_k = 0

    for i in range(0, k + 1):
        current_sum = 0
        for index, number in enumerate(my_list):
            current_sum += (number * index)

        if current_sum > final:
            final = current_sum
            best_k = i
        my_list.appendleft(my_list.pop())

    return f'Best pureness {final} after {best_k} rotations'


test = ([1, 2, 3, 4, 5], 3)
result = best_list_pureness(*test)
print(result)
