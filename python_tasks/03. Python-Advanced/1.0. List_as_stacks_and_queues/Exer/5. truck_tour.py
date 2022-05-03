from collections import deque

n = int(input())

road = deque()

for i in range(n):
    details = [int(x) for x in input().split()]
    road.append(details)


for b in range(n):
    current_fuel = 0
    complete_tour = True

    for detail in road:
        petrol = detail[0]
        distance = detail[1]

        current_fuel += petrol

        if distance > current_fuel:
            road.append(road.popleft())
            complete_tour = False
            break

        current_fuel -= distance

    if complete_tour:
        print(b)
        break





