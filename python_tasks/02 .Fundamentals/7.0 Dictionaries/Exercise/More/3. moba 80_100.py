
my_dict = {}
same_tier = False
while True:
    cmd = input().split(' -> ')

    if cmd[0] == 'Season end':
        break

    if len(cmd) == 3:
        player = cmd[0]
        position = cmd[1]
        skill = int(cmd[2])

        if player not in my_dict:
            my_dict[player] = {}
            my_dict[player][position] = skill

        elif position not in my_dict[player].keys():
            my_dict[player][position] = skill

        elif player in my_dict and position in my_dict[player].keys():
            if skill > my_dict[player][position]:
                my_dict[player][position] = skill

    else:
        cmd_split = ''.join(cmd).split(' vs ')
        player_1 = cmd_split[0]
        player_2 = cmd_split[1]

        if player_1 in my_dict and player_2 in my_dict:
            pos_1 = 'Adc'
            pos_2 = 'Jungle'
            pos_3 = 'Mid'
            pos_4 = 'Support'
            pos_5 = 'Tank'

            if pos_1 in my_dict[player_1].keys() and pos_1 in my_dict[player_2].keys():
                same_tier = True
            elif pos_2 in my_dict[player_1].keys() and pos_2 in my_dict[player_2].keys():
                same_tier = True
            elif pos_3 in my_dict[player_1].keys() and pos_3 in my_dict[player_2].keys():
                same_tier = True
            elif pos_4 in my_dict[player_1].keys() and pos_4 in my_dict[player_2].keys():
                same_tier = True
            elif pos_5 in my_dict[player_1].keys() and pos_5 in my_dict[player_2].keys():
                same_tier = True

            if same_tier:
                player_1_str = sum(my_dict[player_1].values())
                player_2_str = sum(my_dict[player_2].values())

                if player_1_str > player_2_str:
                    del my_dict[player_2]
                elif player_2_str > player_1_str:
                    del my_dict[player_1]

                same_tier = False


for key, value in sorted(my_dict.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f'{key}: {sum(value.values())} skill')
    for pos, points in sorted(value.items(), key=lambda x: (-x[1], x[0])):
        print(f'- {pos} <::> {points}')

