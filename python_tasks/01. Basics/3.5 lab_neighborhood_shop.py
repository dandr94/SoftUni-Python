import math
product = input()
city = input()
quantity = float(input())

sum = 0

if city == 'Sofia':
    if product == 'coffee':
        sum = quantity * 0.50
    elif product == 'water':
        sum = quantity * 0.80
    elif product == 'beer':
        sum = quantity * 1.20
    elif product == 'sweets':
        sum = quantity * 1.45
    elif product == 'peanuts':
        sum = quantity * 1.60

elif city == 'Plovdiv':
    if product == 'coffee':
        sum = quantity * 0.40
    elif product == 'water':
        sum = quantity * 0.70
    elif product == 'beer':
        sum = quantity * 1.15
    elif product == 'sweets':
        sum = quantity * 1.30
    elif product == 'peanuts':
        sum = quantity * 1.50

elif city == 'Varna':
    if product == 'coffee':
        sum = quantity * 0.45
    elif product == 'water':
        sum = quantity * 0.70
    elif product == 'beer':
        sum = quantity * 1.10
    elif product == 'sweets':
        sum = quantity * 1.35
    elif product == 'peanuts':
        sum = quantity * 1.55

print(sum)