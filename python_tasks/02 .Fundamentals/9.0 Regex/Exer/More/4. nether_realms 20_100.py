import re

list_of_participation = input().split(', ')
my_dict = {}

hp_pattern = r'[^0-9\+\-\*\/\.]'
damage_pattern = r'(\+|-)?[0-9]+(\.[0-9]+)?'
del_pattern = r'[\*\\]'

for i in list_of_participation:
    health = 0
    damage = 0
    hp = re.finditer(hp_pattern, i)
    dmg = re.finditer(damage_pattern, i)
    del_count = re.finditer(del_pattern, i)

    for hp_points in hp:
        health += ord(hp_points.group())

    for damage_points in dmg:
        damage += float(damage_points.group())

    for delim in del_count:
        if delim.group() == '*':
            damage *= 2
        elif delim.group() == '/':
            damage /= 2

    if i not in my_dict:
        my_dict[i] = []
        my_dict[i].append(health)
        my_dict[i].append(damage)


for key, value in sorted(my_dict.items(), key=lambda x: x[0]):
    print(f'{key} - {value[0]} health, {value[1]:.2f} damage')

