import math

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
price_gift = float(input())

magnolias_price = magnolias * 3.25
hyacinths_price = hyacinths * 4
roses_price = roses * 3.50
cactus_price = cactus * 8

sum = magnolias_price + hyacinths_price + roses_price + cactus_price
tax = sum * 0.05
sum = sum - tax

if sum >= price_gift:
    diff = sum - price_gift
    print(f'She is left with {math.floor(diff)} leva.')
else:
    diff = price_gift - sum
    print(f'She will have to borrow {math.ceil(diff)} leva.')