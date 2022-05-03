number_of_rows = int(input())
game_on = True
free_chairs = 0
for i in range(1, number_of_rows + 1):
    command_line = input().split()
    seats = command_line[0]
    visitors = int(command_line[1])
    if visitors > len(seats):
        print(f'{visitors - len(seats)} more chairs needed in room {i}')
        game_on = False
    else:
        free_chairs += len(seats) - visitors


if game_on:
    print(f'Game On, {free_chairs} free chairs left')
