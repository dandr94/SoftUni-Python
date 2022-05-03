n = int(input())

current_num = 1
is_current_bigger = False

for i in range(1, n +1):
    for h in range(1, i + 1):

        if current_num > n:
            is_current_bigger = True
            break
        print(f'{current_num}', end=' ')
        current_num += 1

    if is_current_bigger:
        break
    print()
