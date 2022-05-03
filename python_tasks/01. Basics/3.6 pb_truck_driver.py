season = input()
km_in_one_month = float(input())

sum = 0
km_sum = km_in_one_month * 4

if season == 'Spring' or season == 'Autumn' :
    if km_in_one_month <= 5000:
        sum += km_sum * 0.75
    elif km_in_one_month > 5000 and km_in_one_month <= 10_000:
        sum += km_sum * 0.95
    else:
        sum += km_sum * 1.45
elif season == 'Summer':
    if km_in_one_month <= 5000:
        sum += km_sum * 0.90
    elif km_in_one_month > 5000 and km_in_one_month <= 10_000:
        sum += km_sum * 1.10
    else:
        sum += km_sum * 1.45

elif season == 'Winter':
    if km_in_one_month <= 5000:
        sum += km_sum * 1.05
    elif km_in_one_month > 5000 and km_in_one_month <= 10_000:
        sum += km_sum * 1.25
    else:
        sum += km_sum * 1.45

sum -= sum * 0.10

print(f'{sum:.2f}')