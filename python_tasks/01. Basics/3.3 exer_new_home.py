flower = input()
quantity = int(input())
budget = int(input())


sum = 0

if flower == 'Roses':
    sum = quantity * 5
    if quantity > 80:
        sum *= 0.90

elif flower == 'Dahlias':
    sum = quantity * 3.80
    if quantity > 90:
        sum *= 0.85

elif flower == 'Tulips':
    sum = quantity * 2.80
    if quantity > 80:
        sum *= 0.85

elif flower == 'Narcissus':
    sum = quantity * 3
    if quantity < 120:
        sum *= 1.15

elif flower == 'Gladiolus':
    sum = quantity * 2.50
    if quantity < 80:
        sum *= 1.20


if budget >= sum:
    diff = budget - sum
    print(f'Hey, you have a great garden with {quantity} {flower} and {diff:.2f} leva left.')

else:
    diff = sum - budget
    print(f'Not enough money, you need {diff:.2f} leva more.')