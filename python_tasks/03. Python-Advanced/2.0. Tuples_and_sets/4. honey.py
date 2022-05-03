from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey_made = 0


while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_bee > current_nectar:
        bees.appendleft(current_bee)
        continue

    current_symbol = symbols.popleft()

    if current_symbol == '+':
        honey_made += abs(current_bee + current_nectar)
    elif current_symbol == '-':
        honey_made += abs(current_bee - current_nectar)
    elif current_symbol == '*':
        honey_made += abs(current_bee * current_nectar)
    elif current_symbol == '/':
        if current_nectar != 0:
            honey_made += abs(current_bee / current_nectar)


print(f'Total honey made: {honey_made}')

if bees:
    print(f'Bees left: {", ".join([str(x) for x in bees])}')
if nectar:
    print(f'Nectar left: {", ".join([str(x) for x in nectar])}')

