username = input()

cmd = input()

while cmd != 'Sign up':
    cmd_split = cmd.split()
    action = cmd_split[0]

    if action == 'Case':
        way = cmd_split[1]

        if way == 'lower':
            username = username.lower()
        elif way == 'upper':
            username = username.upper()

        print(username)

    elif action == 'Reverse':
        start_index = int(cmd_split[1])
        end_index = int(cmd_split[2])

        if 0 <= start_index < len(username) and end_index < len(username):
            substring = username[start_index:end_index + 1]
            substring = substring[::-1]
            print(substring)

    elif action == 'Cut':
        substring = cmd_split[1]

        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")

    elif action == 'Replace':
        char = cmd_split[1]

        if char in username:
            username = username.replace(char, '*')
            print(username)

    elif action == 'Check':
        char = cmd_split[1]

        if char in username:
            print('Valid')
        else:
            print(f'Your username must contain {char}.')

    cmd = input()

