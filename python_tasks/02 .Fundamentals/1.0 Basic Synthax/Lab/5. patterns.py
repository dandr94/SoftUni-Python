n = int(input())

for a in range(1, n + 1):
    for b in range(1, a + 1):
        print('*', end='')
    print()

for c in range(n, 1, - 1):
    for d in range(c, 1, - 1):
        print('*', end='')
    print()