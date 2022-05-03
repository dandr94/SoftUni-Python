w = int(input())
h = int(input())

cake = h * w
is_cake_left = True

while cake > 0:
    parts = input()
    if parts == 'STOP':
        break
    else:
        if int(parts) > cake:
            is_cake_left = False
            break
        else:
            cake -= int(parts)

if is_cake_left:
    print(f'{cake} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake - int(parts))} pieces more.')
