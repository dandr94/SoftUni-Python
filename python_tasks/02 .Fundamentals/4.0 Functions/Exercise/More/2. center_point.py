import math
x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())


def coordinate_system(x1, y1, x2, y2):

    if math.sqrt(x_1 + y_1) < math.sqrt(x_2 + y_2):
        print(f'({x_1:.0f}, {y_1:.0f})')
    else:
        print(f'({x_2:.0f}, {y_2:.0f})')


coordinate_system(x_1, y_1, x_2, y_2)