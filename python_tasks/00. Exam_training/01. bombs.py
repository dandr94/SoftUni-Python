from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

dict_of_items = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
}

my_items = {}
success = False

while bomb_casings and bomb_effects:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()

    sum_of_two = current_casing + current_effect

    if sum_of_two in dict_of_items:
        item = dict_of_items[sum_of_two]
        if item not in my_items:
            my_items[item] = 1
        else:
            my_items[item] += 1

    else:
        bomb_casings.append(current_casing - 5)
        bomb_effects.appendleft(current_effect)
    if len(my_items) == 3:
        for key, value in my_items.items():
            if value < 3:
                break
        else:
            success = True
            break

if success:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f'Bomb Effects: {", ".join([str(x) for x in bomb_effects])}')
else:
    print('Bomb Effects: empty')

if bomb_casings:
    print(f'Bomb Casings: {", ".join([str(x) for x in bomb_casings])}')
else:
    print(f'Bomb Casings: empty')

for _, item in dict_of_items.items():
    if item not in my_items:
        my_items[item] = 0

for item, amount in sorted(my_items.items()):
    print(f'{item}: {amount}')
