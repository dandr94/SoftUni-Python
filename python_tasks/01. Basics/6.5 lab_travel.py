

destination = input()

money_needed = float(input())

money = input()
sum = 0

while money != 'End':
    money = float(money)
    sum += money
    if sum >= money_needed:
        print(f'Going to {destination}!')
        destination = input()
        if destination == 'End':
            break
        money_needed = float(input())
        sum = 0

    money = input()

# not mine (another solution / better one)

destination = input()

while destination != 'End':
    price_for_vacation = float(input())

    current_money = 0

    while current_money < price_for_vacation:
        price = float(input())
        current_money += price
    else:
        print(f'Going to {destination}!')

    destination = input()





