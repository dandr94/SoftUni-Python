import math

type = input()


if type == 'square':
    num = float(input())
    area = num * num
    print(f'{area:.3f}')

elif type == 'rectangle':
    num_1 = float(input())
    num_2 = float(input())
    area = num_1 * num_2
    print(f'{area:.3f}')

elif type == 'circle':
    rad = float(input())
    area = math.pi * rad * rad
    print(f'{area:.3f}')

elif type == 'triangle':
    num = float(input())
    h = float(input())
    area = 1 / 2 * num * h
    print(f'{area:.3f}')