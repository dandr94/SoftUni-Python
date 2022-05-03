import math
holidays = int(input())

workdays = 365 - holidays
real_time_for_game = workdays * 63 + holidays * 127

if 30_000 > real_time_for_game:
    diff = 30_000 - real_time_for_game
    hours = diff / 60
    minutes = diff % 60
    print('Tom sleeps well')
    print(f'{math.floor(hours)} hours and {minutes} minutes less for play')
else:
    diff = real_time_for_game - 30_000
    hours = diff / 60
    minutes = diff % 60
    print('Tom will run away')
    print(f'{math.floor(hours)} hours and {minutes} minutes more for play')

