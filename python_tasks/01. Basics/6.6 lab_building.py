levels = int(input())
rooms = int(input())

for i in range(levels, 0, - 1):
    for n in range(0, rooms):
        if i == levels:
            print(f'L{i}{n} ', end='')
        elif i % 2 == 0:
            print(f'O{i}{n} ', end='')
        elif i % 2 != 0:
            print(f'A{i}{n} ', end='')
    print()