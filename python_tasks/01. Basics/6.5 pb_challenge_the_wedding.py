men = int(input())
women = int(input())
tables = int(input())

for a in range(1, men + 1):
    for b in range(1, women + 1):
        print(f'({a} <-> {b})', end=' ')
        tables -= 1
        if tables == 0:
            break
    if tables == 0:
        break

