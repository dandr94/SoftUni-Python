str_even_ints = [int(x) for x in input().split('@')]

command = input()

current_position = 0
while command != 'Love!':
    command_split = command.split()
    value = int(command_split[1])

    current_position += value
    if current_position >= len(str_even_ints):
        current_position = 0
        str_even_ints[current_position] -= 2
    else:
        str_even_ints[current_position] -= 2

    if str_even_ints[current_position] == 0:
        print(f"Place {current_position} has Valentine's day.")
    elif str_even_ints[current_position] < 0:
        print(f"Place {current_position} already had Valentine's day.")

    command = input()

print(f"Cupid's last position was {current_position}.")
if sum(str_even_ints) == 0:
    print(f'Mission was successful.')
else:
    x = [num for num in str_even_ints if num > 0]
    print(f'Cupid has failed {len(x)} places.')

