import math
needed_hours = int(input())
days = int(input())
workers_count = int(input())


training = days * 0.10
days_for_work =  (days - training) * 8
overtime_work = workers_count * (2 * days)
sum = days_for_work + overtime_work
sum = math.floor(sum)

if sum >= needed_hours:
    diff = sum - needed_hours
    print(f'Yes!{diff} hours left.')

else:
    diff = needed_hours - sum
    print(f'Not enough time!{diff} hours needed.')

