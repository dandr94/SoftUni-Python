input_number = int(input())


def is_perfect_number(perfect):

    result = 0

    for i in range(1, input_number):
        if input_number % i == 0:
            result += i

    if result == input_number:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."


print(is_perfect_number(input_number))