rent_price = int(input())


cake = rent_price * 20 / 100
drinks = cake - (cake * 0.45)
animator = rent_price / 3
sum = cake + drinks + animator + rent_price
print(sum)