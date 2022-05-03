operator = input()
first_num = int(input())
second_num = int(input())


def solve(a, b, input_operator):
    result = 0
    if operator == 'multiply':
        result = first_num * second_num
    elif operator == 'divide':
        result = first_num // second_num
    elif operator == 'add':
        result = first_num + second_num
    elif operator == 'subtract':
        result = first_num - second_num

    return result


print(solve(first_num, second_num, operator))
