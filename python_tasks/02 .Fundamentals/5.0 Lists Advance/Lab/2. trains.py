number_of_wagons = int(input())
command = input()
train_wagons = [0] * number_of_wagons

while command != 'End':
    command_split = command.split()
    command_action = command_split[0]

    if command_action == 'add':
        add = int(command_split[1])
        train_wagons[-1] += add

    elif command_action == 'insert':
        index = int(command_split[1])
        number_of_people = int(command_split[2])

        train_wagons[index] += number_of_people

    elif command_action == 'leave':
        index = int(command_split[1])
        number_of_people = int(command_split[2])

        train_wagons[index] -= number_of_people

    command = input()

print(train_wagons)
