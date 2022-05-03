from collections import deque


def list_manipulator(list_of_nums, add_or_remove, beg_or_end, *args):
    my_list = deque(list_of_nums)

    if add_or_remove == 'add':
        if beg_or_end == 'beginning':
            [my_list.appendleft(x) for x in args[::-1]]
        else:
            [my_list.append(x) for x in args]
    else:
        if beg_or_end == 'beginning':
            if args:
                for i in args:
                    [my_list.popleft() for _ in range(i) if my_list]
            else:
                if my_list:
                    my_list.popleft()
        else:
            if args:
                for i in args:
                    [my_list.pop() for _ in range(i) if my_list]
            else:
                if my_list:
                    my_list.pop()

    return list(my_list)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
