n = int(input())

spaces = n - 1
stars = 1

for i in range(1, n+1):
    print(f' ' * spaces + ' *' * stars)
    if i == n:
        break
    else:
        spaces -= 1
        stars += 1

for i in range(n, -1, - 1):
    spaces += 1
    stars -= 1
    print(f' ' * spaces + ' *' * stars)