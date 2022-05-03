n = int(input())

p_1 = 0
p_2 = 0
p_3 = 0

for i in range(1, n + 1):
    num = int(input())
    if num % 2 == 0:
        p_1 += 1
    if num % 3 == 0:
        p_2 += 1
    if num % 4 == 0:
        p_3 += 1

p_1 = p_1 / n * 100
p_2 = p_2 / n * 100
p_3 = p_3 / n * 100

print(f'{p_1:.2f}%')
print(f'{p_2:.2f}%')
print(f'{p_3:.2f}%')