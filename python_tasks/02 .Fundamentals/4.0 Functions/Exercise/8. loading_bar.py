number = int(input())


def loading_bar(bar):
    bar = ''
    dots = 10

    for i in range(1, number + 1):
        if i % 10 == 0 :
            bar += '%'
            dots -= 1
    if number != 100:
        print(f'{number}%', end=' ')
        print(f'[{bar}' + dots * '.' + ']')
        print('Still loading...')
    else:
        print(f'{number}% Complete!')
        print(f'[{bar}' + dots * '.' + ']')


loading_bar(number)