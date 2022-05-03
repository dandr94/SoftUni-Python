type_fire_and_amount = input().split('#')

amount_of_water = int(input())

effort = 0
total_fire = 0
print('Cells:')
for fire in type_fire_and_amount:
    new = fire.split(' = ')
    type_fire = new[0]
    amount_of_fire = int(new[1])

    if amount_of_water < amount_of_fire:
        continue

    if type_fire == 'High':
        if 80 < amount_of_fire <= 125:
            amount_of_water -= amount_of_fire
            effort += amount_of_fire * 0.25
        else:
            continue
    elif type_fire == 'Medium':
        if 50 < amount_of_fire <= 80:
            amount_of_water -= amount_of_fire
            effort += amount_of_fire * 0.25
        else:
            continue
    elif type_fire == 'Low':
        if 0 < amount_of_fire <= 50:
            amount_of_water -= amount_of_fire
            effort += amount_of_fire * 0.25
        else:
            continue
    total_fire += amount_of_fire
    print(f' - {amount_of_fire}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
