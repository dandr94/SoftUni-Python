cmd = input()

my_dict = {}

while cmd != 'stop':
    resource = cmd
    quantity = int(input())

    if resource not in my_dict:
        my_dict[resource] = 0

    my_dict[resource] += quantity

    cmd = input()

for key, value in my_dict.items():
    print(f'{key} -> {value}')
