import math

income = float(input())
average_grade = float(input())
minimal_work_payout = float(input())

sum = 0
#Social
if income < minimal_work_payout and average_grade > 4.5 and average_grade < 5.5:
    sum += minimal_work_payout * 0.35
    print(f'You get a social scholarship {math.floor(sum)} BGN')
#Excellent

elif income < minimal_work_payout and average_grade >= 5.50:
    excellent = average_grade * 25
    social = minimal_work_payout * 0.35
    if social > excellent:
        sum += social
        print(f'You get a social scholarship {math.floor(sum)} BGN')
    elif social == excellent:
        sum += excellent
        print(f'You get a scholarship for excellent results {math.floor(sum)} BGN')
    else:
        sum += excellent
        print(f'You get a scholarship for excellent results {math.floor(sum)} BGN')

elif average_grade >= 5.5:
    sum += average_grade * 0.25
    print(f'You get a scholarship for excellent results {math.floor(sum)} BGN')

else:
    print('You cannot get a scholarship!')