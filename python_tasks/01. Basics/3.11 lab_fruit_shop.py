fruit = input()
day = input()
quantity = float(input())

sum = 0
if day == 'Sunday' or day == 'Saturday':
    if fruit == 'banana':
        sum = quantity * 2.70
    elif fruit == 'apple':
        sum = quantity * 1.25
    elif fruit == 'orange':
        sum = quantity * 0.90
    elif fruit == 'grapefruit':
        sum = quantity * 1.60
    elif fruit == 'kiwi':
        sum = quantity * 3.00
    elif fruit == 'pineapple':
        sum = quantity * 5.60
    elif fruit == 'grapes':
        sum = quantity * 4.20
    else:
        print('error')
        quit()

elif day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        sum = quantity * 2.50
    elif fruit == 'apple':
        sum = quantity * 1.20
    elif fruit == 'orange':
        sum = quantity * 0.85
    elif fruit == 'grapefruit':
        sum = quantity * 1.45
    elif fruit == 'kiwi':
        sum = quantity * 2.70
    elif fruit == 'pineapple':
        sum = quantity * 5.50
    elif fruit == 'grapes':
        sum = quantity * 3.85
    else:
        print('error')
        quit()

else:
    print('error')
    quit()

print(f'{sum:.2f}')
