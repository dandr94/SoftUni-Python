capacity = int(input())
fans = int(input())

a_sector = 0
b_sector = 0
v_sector = 0
g_sector = 0

for i in range(1, fans + 1):
    sector = input()

    if sector == 'A':
        a_sector += 1

    elif sector == 'B':
        b_sector += 1

    elif sector == 'V':
        v_sector += 1

    elif sector == 'G':
        g_sector += 1


percent_a_sector = a_sector / fans * 100
percent_b_sector = b_sector / fans * 100
percent_v_sector = v_sector / fans * 100
percent_g_sector = g_sector / fans * 100
percent_all = fans / capacity * 100

print(f'{percent_a_sector:.2f}%')
print(f'{percent_b_sector:.2f}%')
print(f'{percent_v_sector:.2f}%')
print(f'{percent_g_sector:.2f}%')
print(f'{percent_all:.2f}%')