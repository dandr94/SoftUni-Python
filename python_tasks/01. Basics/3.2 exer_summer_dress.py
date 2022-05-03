degrees = int(input())
time_of_the_day = input()

outfit = ' '
shoes = ' '

if time_of_the_day == 'Morning':
    if degrees >= 10 and degrees <= 18:
        sweatshirt = 'Sweatshirt'
        shoes = 'Sneakers'
        print(f"It's {degrees} degrees, get your {sweatshirt} and {shoes}.")
    elif degrees > 18 and degrees <= 24:
        sweatshirt = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {sweatshirt} and {shoes}.")
    elif degrees >= 25:
        sweatshirt = 'T-Shirt'
        shoes = 'Sandals'
        print(f"It's {degrees} degrees, get your {sweatshirt} and {shoes}.")

elif time_of_the_day == 'Afternoon':
    if degrees >= 10 and degrees <= 18:
        sweatshirt = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {sweatshirt} and {shoes}.")
    elif degrees > 18 and degrees <= 24:
        sweatshirt = 'T-Shirt'
        shoes = 'Sandals'
        print(f"It's {degrees} degrees, get your {sweatshirt} and {shoes}.")
    elif degrees >= 25:
        sweatshirt = 'Swim Suit'
        shoes = 'Barefoot'
        print(f"It's {degrees} degrees, get your {sweatshirt} and {shoes}.")

elif time_of_the_day == 'Evening':
    if degrees >= 10 and degrees <= 18:
        sweatshirt = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {sweatshirt} and {shoes}.")
    elif degrees > 18 and degrees <= 24:
        sweatshirt = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {sweatshirt} and {shoes}.")
    elif degrees >= 25:
        sweatshirt = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {sweatshirt} and {shoes}.")