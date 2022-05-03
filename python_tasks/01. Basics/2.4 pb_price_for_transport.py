km = int(input())
day_or_night = input()

taxi_day = 0.79 * km + 0.70
taxi_night = 0.90 * km + 0.70
autobus_day_and_night = 0.09 * km # only allowed if more than 20 km
train_day_and_night = 0.06 * km # only allowed if more than 100 km

if km < 20:
    if day_or_night == "day":
        print(f'{taxi_day:.2f}')
    else:
        print(f'{taxi_night:.2f}')
elif km >= 20 and km < 100:
    print(f'{autobus_day_and_night:.2f}')
else:
    print(f'{train_day_and_night:.2f}')