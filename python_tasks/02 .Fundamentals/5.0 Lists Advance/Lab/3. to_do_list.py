command = input()
notes = [0] * 10

while command != 'End':
    command_split = command.split('-')
    factor_of_importance = int(command_split[0]) - 1
    note = command_split[1]

    notes.pop(factor_of_importance)
    notes.insert(factor_of_importance, note)

    command = input()

result = [element for element in notes if element != 0]
print(result)


