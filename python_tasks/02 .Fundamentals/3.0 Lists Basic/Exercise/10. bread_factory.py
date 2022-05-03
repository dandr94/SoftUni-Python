events = input().split('|')


energy = 100
coins = 100
complete_day = True

for event in events:
    new = event.split('-')
    action = new[0]
    amount = int(new[1])

    if action == 'rest':
        if amount + energy > 100:
            gained = abs(amount + energy - 100) - amount
            energy += gained
            print(f'You gained {gained} energy.')
        else:
            energy += amount
            print(f'You gained {amount} energy.')

        print(f'Current energy: {energy}.')

    elif action == 'order':
        if energy >= 30:
            coins += amount
            energy -= 30
            print(f'You earned {amount} coins.')
        else:
            print('You had to rest!')
            energy += 50

    else:
        if coins > amount:
            coins -= amount
            print(f'You bought {action}.')
        else:
            complete_day = False
            print(f'Closed! Cannot afford {action}.')
            break

if complete_day:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')

