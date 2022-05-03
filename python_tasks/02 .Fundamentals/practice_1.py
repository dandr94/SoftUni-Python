n = int(input())

cars = {}

for i in range(n):
    car = input().split('|')
    vehicle = car[0]
    mileage = int(car[1])
    fuel = int(car[2])

    if vehicle not in cars:
        cars[vehicle] = []
        cars[vehicle].append(mileage)
        cars[vehicle].append(fuel)

cmd = input()

while cmd != 'Stop':
    cmd_split = cmd.split(' : ')
    action = cmd_split[0]
    car = cmd_split[1]

    if action == 'Drive':
        distance = int(cmd_split[2])
        fuel_needed = int(cmd_split[3])

        if cars[car][1] < fuel_needed:
            print('Not enough fuel to make that ride')
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel_needed
            print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")

            if cars[car][0] >= 100_000:
                print(f'Time to sell the {car}!')
                del cars[car]

    elif action == 'Refuel':
        fuel_recharged = int(cmd_split[2])

        if cars[car][1] + fuel_recharged > 75:
            gained = 75 - cars[car][1]
            cars[car][1] += gained
            print(f'{car} refueled with {gained} liters')
        else:
            cars[car][1] += fuel_recharged
            print(f'{car} refueled with {fuel_recharged} liters')

    elif action == 'Revert':
        km = int(cmd_split[2])

        cars[car][0] -= km

        if cars[car][0] < 10_000:
            cars[car][0] = 10_000
        else:
            print(f"{car} mileage decreased by {km} kilometers")

    cmd = input()

for key, value in sorted(cars.items(), key=lambda x: (-x[1][0], x[0])):
    print(f'{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.')