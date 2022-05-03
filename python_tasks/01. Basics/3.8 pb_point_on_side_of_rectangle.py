x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x = float(input())
y = float(input())


first_condition = (x == x_1 or x == x_2) and (y >= y_1 and y <= y_2)
second_condition = (y == y_1 or y == y_2) and (x >= x_1 and x <= x_2)


if first_condition:
    first_condition = True
else:
    first_condition = False
if second_condition:
    second_condition = True
else:
    second_condition = False

if first_condition or second_condition:
    print('Border')
else:
    print('Inside / Outside')