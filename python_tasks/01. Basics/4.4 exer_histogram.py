n = int(input())

p_1 = 0
p_2 = 0
p_3 = 0
p_4 = 0
p_5 = 0


for i in range(1, n + 1):
    num = int(input())
    if num < 200:
        p_1 += 1

    elif num >= 200 and num < 400:
        p_2 += 1

    elif num >= 400 and num < 600:
        p_3 += 1

    elif num >= 600 and num < 800:
        p_4 += 1

    else:
        p_5 += 1


p_1 = p_1 / n * 100
p_2 = p_2 / n * 100
p_3 = p_3 / n * 100
p_4 = p_4 / n * 100
p_5 = p_5 / n * 100

print(f'{p_1:.2f}%')
print(f'{p_2:.2f}%')
print(f'{p_3:.2f}%')
print(f'{p_4:.2f}%')
print(f'{p_5:.2f}%')