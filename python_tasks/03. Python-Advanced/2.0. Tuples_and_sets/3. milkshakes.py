from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
cups_of_milk = deque(int(x) for x in input().split(', '))

milkshakes_prepared = 0

while chocolates and cups_of_milk:
    last_chocolate = chocolates[-1]
    first_cup = cups_of_milk[0]

    if last_chocolate < 1 or first_cup < 1:
        if last_chocolate < 1:
            chocolates.pop()
        if first_cup < 1:
            cups_of_milk.popleft()
        continue

    if last_chocolate == first_cup:
        milkshakes_prepared += 1
        chocolates.pop()
        cups_of_milk.popleft()
        if milkshakes_prepared == 5:
            break
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolates[-1] -= 5

if milkshakes_prepared == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if chocolates:
    print(f'Chocolate: {", ".join(str(x) for x in chocolates)} ')
else:
    print('Chocolate: empty')
if cups_of_milk:
    print(f'Milk: {", ".join(str(x) for x in cups_of_milk)}')
else:
    print('Milk: empty')




