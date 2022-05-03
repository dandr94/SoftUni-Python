def multiply(*args):
    if not args:
        return None

    sum_of_args = 1
    for i in args:
        sum_of_args *= i
    return sum_of_args


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
