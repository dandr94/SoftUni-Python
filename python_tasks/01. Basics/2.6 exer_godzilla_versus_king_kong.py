budget = float(input())
statisticians = int(input())
price_for_dress_for_one_statistician = float(input())


price_statistician = statisticians * price_for_dress_for_one_statistician
decor = budget * 0.10

if statisticians > 150:
    discount = price_statistician * 0.10
    price_statistician = price_statistician - discount

sum = price_statistician + decor

if sum > budget:
    diff = sum - budget
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
else:
    diff = budget - sum
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')