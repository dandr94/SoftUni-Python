import sys
n = int(input())

highest_value = -sys.maxsize
snowball_snow_highest = 0
snowball_time_highest = 0
snowball_quality_highest = 0

for i in range(1, n + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    result = int(snowball_snow / snowball_time) ** snowball_quality

    if result > highest_value:
        highest_value = result
        snowball_snow_highest = snowball_snow
        snowball_time_highest = snowball_time
        snowball_quality_highest = snowball_quality

print(f'{snowball_snow_highest} : {snowball_time_highest} = {highest_value} ({snowball_quality_highest})')