from basic_calculations import *

my_string = input().split()
num_1 = float(my_string[0])
num_2 = int(my_string[2])
operation = my_string[1]

print(f'{basic_calculations(num_1, num_2, operation):.2f}')

