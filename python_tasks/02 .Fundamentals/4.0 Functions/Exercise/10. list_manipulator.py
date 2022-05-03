import sys


def valid_index(collection: list, index: int):
    if 0 <= index < len(collection):
        return True

    return False


def exchange(collection: list, index: int):
    new_list = []

    if not valid_index(collection, index):
        print('Invalid index')
        new_list = collection
    else:
        left_side_list = collection[:index + 1]
        right_side_list = collection[index + 1:]

        for el in right_side_list:
            new_list.append(el)

        for el in left_side_list:
            new_list.append(el)

    return new_list


def max_num(collection: list, lambda_filter):
    max_element = -sys.maxsize
    max_element_index = -1

    for i in range(len(collection)):
        num = collection[i]

        if lambda_filter(num) and num >= max_element:
            max_element = num
            max_element_index = i

    if max_element_index == -1:
        print('No matches')

    return max_element_index


def min_num(collection: list, lambda_filter):
    min_element = sys.maxsize
    min_element_index = -1

    for i in range(len(collection)):
        num = collection[i]

        if lambda_filter(num) and num <= min_element:
            min_element = num
            min_element_index = i

    if min_element_index == -1:
        print('No matches')

    return min_element_index


def first_count_elements_by_criteria(collection: list, count: int, lambda_filter):
    if count > len(collection):
        print('Invalid count')
    else:
        equal_elements = []

        for num in collection:
            if lambda_filter(num) and len(equal_elements) < count:
                equal_elements.append(num)

        print(equal_elements)


def last_count_elements_by_criteria(collection: list, count: int, lambda_filter):
    if count > len(collection):
        print('Invalid count')
    else:
        equal_elements = []

        for i in range(len(collection) - 1, -1, - 1):
            num = collection[i]

            if lambda_filter(num) and len(equal_elements) < count:
                equal_elements.append(num)

        print(equal_elements[::-1])


def collection_to_int(collection: list):
    collection_int = []

    for el in collection:
        collection_int.append(int(el))

    return collection_int


def collection_to_str(collection: list, delimiter: str):
    collection_str = []

    for el in collection:
        collection_str.append(str(el))

    return delimiter.join(collection_str)


elements = input().split(' ')
numbers = collection_to_int(elements)

command = input()

while command != 'end':
    command_split = command.split(' ')
    command_action = command_split[0]

    if command_action == 'exchange':
        index = int(command_split[1])

        numbers = exchange(numbers, index)

    elif command_action == 'max':
        command_filter = command_split[1]

        max_index = -1

        if command_filter == 'even':
            max_index = max_num(numbers, lambda n: n % 2 == 0)
        elif command_filter == 'odd':
            max_index = max_num(numbers, lambda n: n % 2 != 0)

        if max_index != -1:
            print(max_index)

    elif command_action == 'min':
        command_filter = command_split[1]

        min_index = -1

        if command_filter == 'even':
            min_index = min_num(numbers, lambda n: n % 2 == 0)
        elif command_filter == 'odd':
            min_index = min_num(numbers, lambda n: n % 2 != 0)

        if min_index != - 1:
            print(min_index)

    elif command_action == 'first':
        count = int(command_split[1])
        command_filter = command_split[2]

        if command_filter == 'even':
            first_count_elements_by_criteria(numbers, count, lambda n: n % 2 == 0)
        elif command_filter == 'odd':
            first_count_elements_by_criteria(numbers, count, lambda n: n % 2 != 0)

    elif command_action == 'last':
        count = int(command_split[1])
        command_filter = command_split[2]

        if command_filter == 'even':
            last_count_elements_by_criteria(numbers, count, lambda n: n % 2 == 0)
        elif command_filter == 'odd':
            last_count_elements_by_criteria(numbers, count, lambda n: n % 2 != 0)

    command = input()

print(f'[{collection_to_str(numbers, ", ")}]')