input_data = input()
input_data_1 = input()


def data():

    if input_data == 'int':
        return int(input_data_1) * 2
    elif input_data == 'real':
        return f'{float(input_data_1) * 1.5:.2f}'
    elif input_data == 'string':
        return f'${input_data_1}$'


print(data())