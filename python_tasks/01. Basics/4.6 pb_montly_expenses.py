n = int(input())


electricity_sum = 0
water_sum = 0
internet_sum = 0
others_sum = 0


for i in range(1, n +1):
    electricity = float(input())
    electricity_sum += electricity
    water_sum += 20
    internet_sum += 15
    others = electricity + 20 + 15
    others_sum += others + (others * 0.20)

sum = electricity_sum + water_sum + others_sum + internet_sum
medium_price_for_month = sum / n



print(f'Electricity: {electricity_sum:.2f} lv')
print(f'Water: {water_sum:.2f} lv')
print(f'Internet: {internet_sum:.2f} lv')
print(f'Other: {others_sum:.2f} lv')
print(f'Average: {medium_price_for_month:.2f} lv')