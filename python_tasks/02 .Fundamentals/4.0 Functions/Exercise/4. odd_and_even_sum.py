string_of_numbers = input()


def sum_of_odd(numbers_odd):
    result_odd = 0
    result_even = 0

    for i in string_of_numbers:
        if int(i) % 2 != 0:
            result_odd += int(i)
        else:
            result_even += int(i)

    return f'Odd sum = {result_odd}, Even sum = {result_even}'


print(sum_of_odd(string_of_numbers))





