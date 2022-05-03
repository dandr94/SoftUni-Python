input_product = input()
input_quantity = int(input())


def request(product, quantity):
    result = 0

    if input_product == 'coffee':
        result = input_quantity * 1.50
    elif input_product == 'coke':
        result = input_quantity * 1.40
    elif input_product == 'water':
        result = input_quantity * 1.00
    elif input_product == 'snacks':
        result = input_quantity * 2.00

    return f'{result:.2f}'


print(request(input_product, input_quantity))
