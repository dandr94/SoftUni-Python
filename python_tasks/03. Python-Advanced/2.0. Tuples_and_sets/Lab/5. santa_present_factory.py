from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

my_dict = {}
completed = False

while materials and magic_level:
    current_material = materials[-1]
    current_magic_level = magic_level[0]
    mat_idx = materials.index(current_material)
    mag_idx = magic_level.index(current_magic_level)

    sum_of_the_two = current_material * current_magic_level

    if sum_of_the_two == 150:
        if 'Doll' not in my_dict:
            my_dict['Doll'] = 0
        my_dict['Doll'] += 1
        materials.pop()
        magic_level.popleft()
    elif sum_of_the_two == 250:
        if 'Wooden train' not in my_dict:
            my_dict['Wooden train'] = 0
        my_dict['Wooden train'] += 1
        materials.pop()
        magic_level.popleft()
    elif sum_of_the_two == 300:
        if 'Teddy bear' not in my_dict:
            my_dict['Teddy bear'] = 0
        my_dict['Teddy bear'] += 1
        materials.pop()
        magic_level.popleft()
    elif sum_of_the_two == 400:
        if 'Bicycle' not in my_dict:
            my_dict['Bicycle'] = 0
        my_dict['Bicycle'] += 1
        materials.pop()
        magic_level.popleft()

    else:
        if materials[mat_idx] == 0 and magic_level[mag_idx] == 0:
            materials.pop()
            magic_level.popleft()
        elif materials[mat_idx] == 0:
            materials.pop()
        elif magic_level[mag_idx] == 0:
            magic_level.popleft()
        elif sum_of_the_two < 0:
            materials.append(materials.pop() + magic_level.popleft())
        elif sum_of_the_two < 150:
            magic_level.popleft()
            materials[mat_idx] += 15



if 'Doll' and 'Wooden train' in my_dict.keys():
    completed = True
if 'Teddy bear' and 'Bicycle' in my_dict.keys():
    completed = True

if completed:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join(str(x) for x in materials[::-1])}')
if magic_level:
    print(f'Magic left: {", ".join(str(x) for x in magic_level)}')

for toy, amount in sorted(my_dict.items()):
    print(f'{toy}: {amount}')