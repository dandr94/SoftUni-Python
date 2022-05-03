from fibonacci_sequence import *

list_of_numbers = []
while True:
    cmd = input().split()
    action = cmd[0]

    if action == 'Stop':
        break

    if cmd[0] == 'Create':
        list_of_numbers.clear()
        number_of_times = int(cmd[2])
        for i in range(number_of_times):
            list_of_numbers.append(fibonacci(i))
        print(' '.join([str(x) for x in list_of_numbers]))

    elif cmd[0] == 'Locate':
        locate_number = int(cmd[1])
        try:
            print(f'The number {locate_number} is at index {list_of_numbers.index(locate_number)}')
        except ValueError:
            print(f'The number {locate_number} is not in the sequence')




