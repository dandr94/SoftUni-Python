budget = int(input())
season = input()
fishermen = int(input())

sum = 0

if season == 'Spring':
    sum += 3000

elif season == 'Summer' or season == 'Autumn':
    sum += 4200

else:
    sum += 2600

if fishermen <= 6:
    sum *= 0.90

elif fishermen <= 11:
    sum *= 0.85

else:
    sum *= 0.75

if season != 'Autumn' and fishermen % 2 == 0:
    sum *= 0.95

if sum > budget:
    diff = sum - budget
    print(f'Not enough money! You need {diff:.2f} leva.')
else:
    diff = budget - sum
    print(f'Yes! You have {diff:.2f} leva left.')