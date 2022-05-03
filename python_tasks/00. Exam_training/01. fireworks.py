from collections import deque

fireworks_effect = deque([int(x) for x in input().split(', ')])
explosive_power = [int(x) for x in input().split(', ')]

my_dict = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}
is_completed = False
while fireworks_effect and explosive_power:
    current_firework = fireworks_effect.popleft()
    if current_firework < 1:
        continue
    current_explosive = explosive_power.pop()
    if current_explosive < 1:
        fireworks_effect.appendleft(current_firework)
        continue

    sum_of_the_two = current_firework + current_explosive

    if sum_of_the_two % 3 == 0 and sum_of_the_two % 5 == 0:
        my_dict['Crossette Fireworks'] += 1

    elif sum_of_the_two % 3 == 0 and sum_of_the_two % 5 != 0:
        my_dict['Palm Fireworks'] += 1

    elif sum_of_the_two % 3 != 0 and sum_of_the_two % 5 == 0:
        my_dict['Willow Fireworks'] += 1

    else:
        explosive_power.append(current_explosive)
        if current_firework - 1 > 0:
            fireworks_effect.append(current_firework - 1)

    for key, value in my_dict.items():
        if value < 3:
            break
    else:
        is_completed = True
        break

if is_completed:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effect:
    print(f'Firework Effects left: {", ".join([str(x) for x in fireworks_effect])}')
if explosive_power:
    print(f'Explosive Power left: {", ".join([str(x) for x in explosive_power])}')

for key, value in my_dict.items():
    print(f'{key}: {value}')
