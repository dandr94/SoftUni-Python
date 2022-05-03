budget = float(input())
season = input()

class_car = ''
car = ''
sum = 0

if budget <= 100:
    class_car = 'Economy class'
    if season == 'Summer':
        car = 'Cabrio'
        sum += budget * 0.35
    elif season == 'Winter':
        car = 'Jeep'
        sum += budget * 0.65

elif budget > 100 and budget <= 500:
    class_car = 'Compact class'
    if season == 'Summer':
        car = 'Cabrio'
        sum += budget * 0.45
    elif season == 'Winter':
        car = 'Jeep'
        sum += budget * 0.80

elif budget > 500:
    class_car = 'Luxury class'
    car = 'Jeep'
    sum += budget * 0.90

print(f'{class_car}')
print(f'{car} - {sum:.2f}')