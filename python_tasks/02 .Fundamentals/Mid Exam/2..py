def is_valid_index(index: int):
    if 0 <= index < len(name_of_weapon):
        return True

    return False


name_of_weapon = input().split('|')

cmd = input()

while cmd != 'Done':
    cmd_split = cmd.split()
    action = cmd_split[0]

    if action == 'Add':
        particle = cmd_split[1]
        index = int(cmd_split[2])

        if is_valid_index(index):
            name_of_weapon.insert(index, particle)

    elif action == 'Remove':
        index = int(cmd_split[1])

        if is_valid_index(index):
            name_of_weapon.pop(index)

    elif action == 'Check' and cmd_split[1] == 'Even':
        string = ''
        for i in range(len(name_of_weapon)):
            if i % 2 == 0:
                string += f'{name_of_weapon[i]} '
        print(string)

    elif action == 'Check' and cmd_split[1] == 'Odd':
        string = ''
        for i in range(len(name_of_weapon)):
            if i % 2 != 0:
                string += f'{name_of_weapon[i]} '
        print(string)

    cmd = input()
print(f'You crafted {"".join(name_of_weapon)}!')