import math

x_vineyard = int(input())
y_grapes = float(input())
z_wine = int(input())
workers = int(input())

grapes = x_vineyard * y_grapes
x_wine = (grapes * 0.40) / 2.5


if x_wine >= z_wine:
    diff = x_wine - z_wine
    diff_per_worker = diff / workers
    print(f'Good harvest this year! Total wine: {math.floor(x_wine)} liters.')
    print(f'{math.ceil(diff)} liters left -> {math.ceil(diff_per_worker)} liters per person.')
else:
    diff = z_wine - x_wine
    print(f'It will be a tough winter! More {math.floor(diff)} liters wine needed.')


