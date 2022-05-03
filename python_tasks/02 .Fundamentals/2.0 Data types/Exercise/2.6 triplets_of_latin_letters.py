n = int(input())


for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(1, n + 1):
            print(f'{chr(a + 96)}{chr(b + 96)}{chr(c + 96)}')