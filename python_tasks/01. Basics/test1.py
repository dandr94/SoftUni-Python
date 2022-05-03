n = int(input())

spaces = n - 1
stars = 1


print(f' ' * spaces + '*')
for i in range(1, n):
    print(f' ' * (spaces - 1) + ' *' * (stars + 1))

