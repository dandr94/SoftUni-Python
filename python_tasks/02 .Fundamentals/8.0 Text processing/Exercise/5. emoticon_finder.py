some_string = input()

for i in range(len(some_string)):
    if some_string[i] == ':':
        print(f'{some_string[i] + some_string[i + 1]}')