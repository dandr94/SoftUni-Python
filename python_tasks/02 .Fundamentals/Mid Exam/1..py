import math

biscuits_per_day_per_person = int(input())
workers_count = int(input())
competing_factory = int(input()) # 30 days

sum_biscuits = 0

for i in range(30):
    if i % 3 == 0:
        left_over = (biscuits_per_day_per_person * workers_count) * 0.75
        left_over = math.floor(left_over)
        sum_biscuits += left_over
    else:
        sum_biscuits += biscuits_per_day_per_person * workers_count

print(f'You have produced {sum_biscuits} biscuits for the past month.')

if sum_biscuits > competing_factory:
    percent = (sum_biscuits - competing_factory) / competing_factory * 100
    print(f'You produce {percent:.2f} percent more biscuits.')
else:
    percent = (competing_factory - sum_biscuits) / competing_factory * 100
    print(f'You produce {percent:.2f} percent less biscuits.')


