age = int(input())
price_laundry = float(input())
toy_price = int(input())

odd_toys = 0
even_money = 0
stolen_money = 0

for i in range(1, age +1):
    if i % 2 == 0:
        stolen_money += 1
        if even_money == 0:
            even_money = 10
        else:
            even_money += i * 5
    else:
        odd_toys += 1

sold_toys_sum = odd_toys * toy_price
sum = sold_toys_sum + even_money - stolen_money

if sum >= price_laundry:
    diff = sum - price_laundry
    print(f'Yes! {diff:.2f}')
else:
    diff = price_laundry - sum
    print(f'No! {diff:.2f}')