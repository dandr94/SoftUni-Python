dish_washing_liquid_bottles = int(input())

dish_washing_liquid = 750 * dish_washing_liquid_bottles

count = 0
dishes = 0
pots = 0

vessel_quantity = input()

while vessel_quantity != 'End':
    vessel_quantity = int(vessel_quantity)
    count += 1
    if count == 3:
        dish_washing_liquid -= 15 * vessel_quantity
        if dish_washing_liquid < 0:
            break
        else:
            count = 0
            pots += vessel_quantity
    else:
        dish_washing_liquid -= 5 * vessel_quantity
        if dish_washing_liquid < 0:
            break
        else:
            dishes += vessel_quantity
    vessel_quantity = input()

if dish_washing_liquid >= 0:
    print('Detergent was enough!')
    print(f'{dishes} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {dish_washing_liquid} ml.')
else:
    print(f'Not enough detergent, {abs(dish_washing_liquid)} ml. more necessary!')