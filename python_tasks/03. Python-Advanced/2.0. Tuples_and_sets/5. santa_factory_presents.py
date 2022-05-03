from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

presents = {150: 'Doll',
            250: 'Wooden train',
            300: 'Teddy bear',
            400: 'Bicycle'
            }

my_dict = {}

while materials and magic_level:
    current_mat = materials.pop()
    current_magic = magic_level.popleft()

    sum_of_the_two = current_mat * current_magic

    if current_mat == 0 and current_magic == 0:
        continue
    if current_mat == 0:
        magic_level.appendleft(current_magic)
        continue
    if current_magic == 0:
        materials.append(current_mat)
        continue

    if sum_of_the_two < 0:
        materials.append(current_mat + current_magic)
    elif sum_of_the_two in presents:
        present = presents[sum_of_the_two]
        if present not in my_dict:
            my_dict[present] = 1
        else:
            my_dict[present] += 1
    else:
        materials.append(current_mat + 15)

is_completed = ('Doll' in my_dict and 'Wooden train' in my_dict) or \
               ('Teddy bear' in my_dict and 'Bicycle' in my_dict)

if is_completed:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials[::-1]])}')
if magic_level:
    print(f'Magic left: {", ".join([str(x) for x in magic_level])}')

for key, value in sorted(my_dict.items()):
    print(f'{key}: {value}')
