

capacity = 255

n = int(input())

litres_in = 0
for i in range(1, n + 1):
    pouring = int(input())

    if pouring > capacity:
        print('Insufficient capacity!')
    else:
        capacity -= pouring
        litres_in += pouring

print(f'{litres_in}')