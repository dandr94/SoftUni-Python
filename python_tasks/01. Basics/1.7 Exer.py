berries_price = float(input())
bananas_in_kg = float(input())
oranges_in_kg = float(input())
raspberries_in_kg = float(input())
berries_in_kg = float(input())

raspberries_price = berries_price / 2
oranges_price = raspberries_price - (0.4 * raspberries_price)
bananas_price = raspberries_price - (0.8 * raspberries_price)

sum_raspberries = raspberries_in_kg * raspberries_price
sum_oranges = oranges_in_kg * oranges_price
sum_bananas = bananas_in_kg * bananas_price
sum_berries = berries_in_kg * berries_price

sum_all = sum_oranges + sum_berries + sum_bananas + sum_raspberries
print(sum_all)



