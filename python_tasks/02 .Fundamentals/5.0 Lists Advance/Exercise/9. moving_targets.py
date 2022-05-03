sequence_of_targets = input().split()
sequence_of_targets_to_int = list(map(int, sequence_of_targets))

command = input()


while command != 'End':
    command_split = command.split()
    command_action = command_split[0]
    index_num = 0
    value = 0

    if command_action == 'Shoot':
        index_num = int(command_split[1])
        value = int(command_split[2])
        if 0 <= index_num < len(sequence_of_targets_to_int):
            sequence_of_targets_to_int[index_num] -= value
            if sequence_of_targets_to_int[index_num] <= 0:
                sequence_of_targets_to_int.pop(index_num)

    elif command_action == 'Add':
        index_num = int(command_split[1])
        value = int(command_split[2])

        if 0 <= index_num < len(sequence_of_targets_to_int):
            sequence_of_targets_to_int.insert(index_num, value)
        else:
            print('Invalid placement!')

    elif command_action == 'Strike':
        index_num = int(command_split[1])
        value = int(command_split[2])
        start = index_num - value
        end = index_num + value
        if start >= 0 and end < len(sequence_of_targets_to_int):
            del sequence_of_targets_to_int[start: end + 1]
        else:
            print('Strike missed!')

    command = input()

print('|'.join(map(str, sequence_of_targets_to_int)))



