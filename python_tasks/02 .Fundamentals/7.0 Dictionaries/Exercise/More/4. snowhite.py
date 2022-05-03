my_dict = {}

while True:
    cmd = input().split(' <:> ')

    if cmd[0] == 'Once upon a time':
        break

    name = cmd[0]
    hat_color = cmd[1]
    physics = int(cmd[2])

    if hat_color not in my_dict:
        my_dict[hat_color] = {}
        my_dict[hat_color][name] = physics

    elif hat_color in my_dict and name not in my_dict[hat_color]:
        my_dict[hat_color][name] = physics

    elif hat_color in my_dict and name in my_dict[hat_color]:
        if physics > my_dict[hat_color][name]:
            my_dict[hat_color][name] = physics

points_dict = {}
color_dict = {}

for key, value in sorted(my_dict.items(), key=lambda x: -len(x[1])):
    for k, v in sorted(value.items(), key= lambda x: -x[1]):
        print(f'({key}), {k} <-> {v}')

