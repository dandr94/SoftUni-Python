
year = input()
holidays = int(input())
weekends = int(input())

weekends_in_sofia = 48 - weekends
saturday_games_in_sofia = weekends_in_sofia * 3 / 4
holidays_in_sofia = holidays * 2 / 3

sum = saturday_games_in_sofia + weekends + holidays_in_sofia

if year == 'leap':
    sum += sum * 0.15
    print(int(sum))
else:
    print(int(sum))