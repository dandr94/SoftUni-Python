import os

while True:
    cmd = input().split('-')
    command = cmd[0]
    if command == 'End':
        break

    file_name = cmd[1]

    if command == 'Create':
        with open(file_name, 'w'):
            pass
    elif command == 'Add':
        content = cmd[2]
        with open(file_name, 'a') as file:
            file.write(content + '\n')

    elif command == 'Replace':
        old_string, new_string = cmd[2:]
        try:
            with open(file_name, 'r') as file:
                content = file.read()

            with open(file_name, 'w') as file:
                content = content.replace(old_string, new_string)
                file.write(content)
        except FileNotFoundError:
            print('An error occurred')

    elif command == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:  # as info: .. returns more information about the error /print(info)
            print('An error occurred')
