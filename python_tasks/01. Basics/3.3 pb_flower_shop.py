chrysanthemums_bought = int(input())
roses_bought = int(input())
tulips_bought = int(input())
season = input()
is_it_holiday = input()

sum = 0
quantity = chrysanthemums_bought + roses_bought + tulips_bought

if season == 'Summer' or season == 'Spring':
    if is_it_holiday == 'Y':
        sum += chrysanthemums_bought * (2 + (2 * 0.15)) + roses_bought * (4.10 + (4.10 * 0.15)) \
        + tulips_bought * (2.50 + (2.50 * 0.15))
    else:
        sum += chrysanthemums_bought * 2 + roses_bought * 4.10 + tulips_bought * 2.50
    if season == 'Spring':
        if tulips_bought > 7:
            sum -= sum * 0.05

else:
    if is_it_holiday == 'Y':
        sum += chrysanthemums_bought * (3.75 + (3.75 * 0.15)) + roses_bought * (4.50 + (4.50 * 0.15)) \
        + tulips_bought * (4.15 + (4.15 * 0.15))
    else:
        sum += chrysanthemums_bought * 3.75 + roses_bought * 4.50 + tulips_bought * 4.15
    if season == 'Winter':
        if roses_bought >= 10:
            sum -= sum * 0.10

if quantity > 20:
    sum -= sum * 0.20

sum += 2

print(f'{sum:.2f}')