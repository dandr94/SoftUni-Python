import sys

input_num_1 = int(input())
input_num_2 = int(input())
input_num_3 = int(input())


def smallest_of_three_numbers(num1, num2, num3):

    result = 0

    if input_num_1 < input_num_2 and input_num_1 < input_num_3:
        result = input_num_1
    elif input_num_2 < input_num_1 and input_num_2 < input_num_3:
        result = input_num_2
    elif input_num_3 < input_num_2 and input_num_3 < input_num_1:
        result = input_num_3

    return result


print(smallest_of_three_numbers(input_num_1, input_num_2, input_num_3))