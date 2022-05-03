month = input()
nights = int(input())


studio = 0
apartments = 0

if month == 'May' or month == 'October':
    studio += nights * 50
    apartments += nights * 65
    if nights > 7 and nights <= 14:
        studio -= studio * 0.05
    elif nights > 14:
        studio -= studio * 0.30
        apartments -= apartments * 0.10

elif month == 'June' or month == 'September':
    studio += nights * 75.20
    apartments += nights * 68.70
    if nights > 14:
        studio -= studio * 0.20
        apartments -= apartments * 0.10


elif month == 'July' or month == 'August':
    studio += nights * 76
    apartments += nights * 77
    if nights > 14:
        apartments -= apartments * 0.10


print(f'Apartment: {apartments:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')