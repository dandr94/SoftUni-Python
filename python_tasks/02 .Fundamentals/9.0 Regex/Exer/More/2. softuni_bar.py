import re

cmd = input()

pattern = r'\%(?P<customer>[A-Z][a-z]+)\%[^|$%.]*\<(?P<product>\w+)\>[^|$%.]*\|(?P<quantity>\d+)\|[^|$%.]*?(?P<price>\d+([.]\d+)?)\$'

total_income = 0

while cmd != 'end of shift':
    result = re.finditer(pattern, cmd)

    for i in result:
        total_price = float(i.group("price")) * int(i.group("quantity"))
        print(f'{i.group("customer")}: {i.group("product")} - {total_price:.2f}')
        total_income += total_price

    cmd = input()

print(f'Total income: {total_income:.2f}')