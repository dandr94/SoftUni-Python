budget = float(input())
category = input()
people = int(input())

transport = 0
sum = 0


if 1 <= people <= 4:
    transport = budget * 0.75

elif 5 <= people <= 9:
    transport = budget * 0.60

elif 10 <= people <= 24:
    transport = budget * 0.50

elif 25 <= people <= 49:
    transport = budget * 0.40

elif people >= 50:
    transport = budget * 0.25

if category == 'VIP':
    sum += 499.99 * people
else:
    sum += 249.99 * people

sum = transport + sum


if budget >= sum:
    diff = budget - sum
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    diff = sum - budget
    print(f'Not enough money! You need {diff:.2f} leva.')


