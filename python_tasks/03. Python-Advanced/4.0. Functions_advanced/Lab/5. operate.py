def operate(operator, *args):
    sum_of_numbers = args[0]

    for i in args[1:]:
        if operator == '+':
            sum_of_numbers += i
        elif operator == '-':
            sum_of_numbers -= i
        elif operator == '*':
            sum_of_numbers *= i
        elif operator == '/':
            if i == 0:
                continue
            sum_of_numbers /= i

    return sum_of_numbers


