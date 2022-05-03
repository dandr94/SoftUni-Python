n = int(input())

parking = {}


for i in range(1, n + 1):
    cmd = input().split()
    action = cmd[0]
    name = cmd[1]

    if action == 'register':
        plate_number = cmd[2]

        if name not in parking:
            parking[name] = plate_number
            print(f'{name} registered {plate_number} successfully')
        else:
            print(f'ERROR: already registered with plate number {plate_number}')

    elif action == 'unregister':

        if name not in parking:
            print(f'ERROR: user {name} not found')
        else:
            print(f'{name} unregistered successfully')
            parking.pop(name)


for name, plate in parking.items():
    print(f'{name} => {plate}')