price_kg_vegetables = float(input())
price_kg_fruits = float(input())
sum_kg_vegetables = int(input())
sum_kg_fruits = int(input())

euro_to_bgn = 1.94

sum_vegetables = price_kg_vegetables * sum_kg_vegetables
convert_price_vegetables = sum_vegetables / euro_to_bgn
sum_fruits = price_kg_fruits * sum_kg_fruits
convert_price_fruits = sum_fruits / euro_to_bgn
all = convert_price_fruits + convert_price_vegetables
print(f'{all:.2f}')