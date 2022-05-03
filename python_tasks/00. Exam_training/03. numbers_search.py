def numbers_searching(*args):
    missing = 0
    duplicates = []

    for num in range(min(args), max(args) + 1):
        if num not in args:
            missing = num
        else:
            count = args.count(num)
            if count > 1:
                duplicates.append(num)

    return [missing, duplicates]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
