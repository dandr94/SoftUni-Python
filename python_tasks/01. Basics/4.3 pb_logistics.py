n = int(input())


sum_weight = 0
minibus = 0
truck = 0
train = 0

for i in range(1, n + 1):
    weight = int(input())
    sum_weight += weight

    if weight <= 3:
        minibus += weight
    elif weight > 3 and weight <= 11:
        truck += weight
    else:
        train += weight


price_minibus = minibus * 200
price_truck = truck * 175
price_train = train * 120
sum_price = price_minibus + price_truck + price_train
medium_price = sum_price / sum_weight

percent_minibus = minibus / sum_weight * 100
percent_truck = truck / sum_weight * 100
percent_train = train / sum_weight * 100

print(f'{medium_price:.2f}')
print(f'{percent_minibus:.2f}%')
print(f'{percent_truck:.2f}%')
print(f'{percent_train:.2f}%')



