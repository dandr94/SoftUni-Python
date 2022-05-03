vacation_price = float(input())

quantity_puzzles = int(input())
quantity_dolls = int(input())
quantity_teddy_bears = int(input())
quantity_minions = int(input())
quantity_trucks = int(input())

puzzles_price = quantity_puzzles * 2.60
dolls_price = quantity_dolls * 3
teddy_bears_price = quantity_teddy_bears * 4.10
minions_price = quantity_minions * 8.20
trucks_price = quantity_trucks * 2
sum_toys = quantity_puzzles + quantity_dolls + quantity_teddy_bears + quantity_minions + quantity_trucks
sum_price = puzzles_price + dolls_price + teddy_bears_price + minions_price + trucks_price

if sum_toys >= 50:
    discount = sum_price * 25/100
    sum_price = sum_price - discount

rent = sum_price * 10 / 100
final = sum_price - rent

if final >= vacation_price:
    diff = final - vacation_price
    print(f'Yes! {diff:.2f} lv left.')
else:
    diff = vacation_price - final
    print(f'Not enough money! {diff:.2f} lv needed.')