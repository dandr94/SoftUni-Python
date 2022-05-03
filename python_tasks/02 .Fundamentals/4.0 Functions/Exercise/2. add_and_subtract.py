input_number_1 = int(input())
input_number_2 = int(input())
input_number_3 = int(input())


def sum_number():

    result = input_number_1 + input_number_2

    return result


def subtract():

    subtract_result = sum_number() - input_number_3

    return subtract_result


def add_and_subtract(num1, num2, num3):

    return subtract()


print(add_and_subtract(input_number_1, input_number_2, input_number_3))