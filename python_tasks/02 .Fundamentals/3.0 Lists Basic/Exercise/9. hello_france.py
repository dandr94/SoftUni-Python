items_and_prices = input().split('|')
budget = float(input())

old_prices = 0
sold_price = 0


for items in items_and_prices:
    new = items.split('->')
    item = new[0]
    price = float(new[1])

    if item == 'Clothes' and price <= 50 and budget >= price:
        budget -= price

    elif item == 'Shoes' and price <= 35 and budget >= price:
        budget -= price

    elif item == 'Accessories' and price <= 20.50 and budget >= price:
        budget -= price
    else:
        continue

    old_prices += price
    new_price = price + (price * 0.40)
    sold_price += price + (price * 0.40)
    print(f'{new_price:.2f}', end=' ')

print()
profit = sold_price - old_prices
print(f'Profit: {profit:.2f}')
if budget + sold_price >= 150:
    print('Hello, France!')
else:
    print('Time to go.')