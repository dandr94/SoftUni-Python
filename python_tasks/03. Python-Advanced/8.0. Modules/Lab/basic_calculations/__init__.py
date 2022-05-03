def basic_calculations(number_1, number_2, sign):
    result = number_1

    if sign == '/':
        try:
            result /= number_2
        except ZeroDivisionError:
            print('Cannot divide by zero')
        finally:
            exit()
    elif sign == '*':
        result *= number_2
    elif sign == '-':
        result -= number_2
    elif sign == '+':
        result += number_2
    elif sign == '^':
        result **= number_2

    return result
