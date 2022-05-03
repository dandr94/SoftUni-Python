def force_user_exist(force_dict: dict, username: str):
    for user_list in force_dict.values():
        if username in user_list:
            return True

    return False


def remove_user(force_dict: dict, user: str):
    for side, users in force_dict.items():
        if user in users:
            force_dict[side].remove(user)


def initial_join(force_dict: dict, side: str, username: str):
    if side not in force_side.keys() and not force_user_exist(force_dict, username):
        force_side[side] = []
        force_side[side].append(username)
    elif not force_user_exist(force_dict, username):
        force_side[side].append(username)


def join_side(force_dict: dict, side: str, username: str):
    if side not in force_side.keys() and not force_user_exist(force_dict, username):
        force_side[side] = []
        force_side[side].append(username)
    elif not force_user_exist(force_dict, username):
        if side not in force_side.keys():
            force_dict[side] = []
        force_side[side].append(username)
    elif force_user_exist(force_dict, username):
        remove_user(force_dict, username)
        if side not in force_side.keys():
            force_dict[side] = []
        force_side[side].append(username)

    print(f'{username} joins the {side} side!')


force_side = {}

cmd = input()

while cmd != 'Lumpawaroo':

    if '|' in cmd:
        cmd_split = cmd.split(' | ')
        force_side_input = cmd_split[0]
        force_user_input = cmd_split[1]

        initial_join(force_side, force_side_input, force_user_input)

    elif '->' in cmd:
        cmd_split = cmd.split(' -> ')
        force_user_input = cmd_split[0]
        force_side_input = cmd_split[1]

        join_side(force_side, force_side_input, force_user_input)

    cmd = input()


for side, users in sorted(force_side.items(), key=lambda x: (-(len(x[1])), x[0])):
    if len(users) > 0:
        print(f'Side: {side}, Members: {len(users)}')
        for user in sorted(users):
            print(f'! {user}')