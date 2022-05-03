num_1 = int(input())
num_2 = int(input())


def factorial(num1, num2):
    num_1_sum = num_1
    num_2_sum = num_2

    for i in range(num_1 - 1, 0, - 1):
        num_1_sum *= i

    for b in range(num_2 - 1, 0, - 1):
        num_2_sum *= b

    return f'{num_1_sum / num_2_sum:.2f}'


print(factorial(num_1, num_2))