days = int(input())
hours_per_day = int(input())

sum_money = 0

for day in range(1, days + 1):
    sum_per_day = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            sum_per_day += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            sum_per_day += 1.25
        else:
            sum_per_day += 1
    sum_money += sum_per_day
    print(f'Day: {day} - {sum_per_day:.2f} leva')

print(f'Total: {sum_money:.2f} leva')