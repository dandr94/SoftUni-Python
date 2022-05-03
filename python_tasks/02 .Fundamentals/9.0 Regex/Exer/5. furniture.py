import re


pattern = r'^>>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+\.?\d+)!(?P<quantity>\d+)$'
furniture = []
total_price = 0
cmd = input()

while cmd != 'Purchase':
    match = re.match(pattern, cmd)
    if match:
        furniture.append(match.group('furniture'))
        price = float(match.group('price'))
        quantity = int(match.group('quantity'))
        total_price += price * quantity

    cmd = input()

print('Bought furniture:')
for i in furniture:
    print(i)

print(f'Total money spend: {total_price:.2f}')