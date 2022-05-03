from collections import deque


def check_if_completed(my_dictionary):
    if 'Gemstone' in my_dictionary and 'Porcelain Sculpture' in my_dictionary or \
            'Gold' in my_dictionary and 'Diamond Jewellery' in my_dictionary:
        return True
    return False


materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

my_dict = {}

is_completed = False

while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()

    sum_of_both = current_material + current_magic

    if sum_of_both < 100:
        if sum_of_both % 2 == 0:
            current_material *= 2
            current_magic *= 3
            sum_of_both = current_material + current_magic
        else:
            sum_of_both *= 2

    elif sum_of_both > 499:
        sum_of_both /= 2

    if 100 <= sum_of_both < 200:
        if 'Gemstone' not in my_dict:
            my_dict['Gemstone'] = 0
        my_dict['Gemstone'] += 1

    elif 200 <= sum_of_both < 300:
        if 'Porcelain Sculpture' not in my_dict:
            my_dict['Porcelain Sculpture'] = 0
        my_dict['Porcelain Sculpture'] += 1

    elif 300 <= sum_of_both < 400:
        if 'Gold' not in my_dict:
            my_dict['Gold'] = 0
        my_dict['Gold'] += 1

    elif 400 <= sum_of_both < 500:
        if 'Diamond Jewellery' not in my_dict:
            my_dict['Diamond Jewellery'] = 0
        my_dict['Diamond Jewellery'] += 1


completed = check_if_completed(my_dict)

if completed:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials])}')
if magic_level:
    print(f'Magic left: {", ".join([str(x) for x in magic_level])}')

for key, value in sorted(my_dict.items()):
    print(f'{key}: {value}')
