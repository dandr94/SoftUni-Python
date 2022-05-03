n_1 = int(input())
n_2 = int(input())
operator = input()

sum = 0

if operator == '+' or operator == '-' or operator == '*':
    if operator == '+':
        sum = n_1 + n_2
        if sum % 2 == 0:
            print(f'{n_1} {operator} {n_2} = {sum} - even')
        else:
            print(f'{n_1} {operator} {n_2} = {sum} - odd')

    elif operator == '-':
        sum = n_1 - n_2
        if sum % 2 == 0:
            print(f'{n_1} {operator} {n_2} = {sum} - even')
        else:
            print(f'{n_1} {operator} {n_2} = {sum} - odd')

    elif operator == '*':
        sum = n_1 * n_2
        if sum % 2 == 0:
            print(f'{n_1} {operator} {n_2} = {sum} - even')
        else:
            print(f'{n_1} {operator} {n_2} = {sum} - odd')

elif operator == '/':
    if n_2 == 0:
        print(f'Cannot divide {n_1} by zero')
        quit()
    sum = n_1 / n_2
    print(f'{n_1} {operator} {n_2} = {sum:.2f}')


elif operator == '%':
    if n_2 == 0:
        print(f'Cannot divide {n_1} by zero')
        quit()
    sum = n_1 % n_2
    print(f'{n_1} {operator} {n_2} = {sum}')
