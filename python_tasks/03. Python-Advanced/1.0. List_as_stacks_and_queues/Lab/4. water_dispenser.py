from collections import deque

starting_quantity = int(input())

que_names = deque()

while True:
    names = input()

    if names == 'Start':
        break

    que_names.append(names)


while True:
    cmd = input().split()

    if cmd[0] == 'End':
        break
    elif len(cmd) < 2:
        litters = int(cmd[0])

        if litters <= starting_quantity:
            starting_quantity -= litters
            print(f'{que_names.popleft()} got water')
        else:
            print(f'{que_names.popleft()} must wait')

    elif len(cmd) > 1:
        litters = int(cmd[1])
        starting_quantity += litters

print(f'{starting_quantity} liters left')
