n = int(input())
count = 0

for x_1 in range(0, n +1):
    for x_2 in range(0, n + 1):
        for x_3 in range(0, n + 1):
            if x_1 + x_2 + x_3 == n:
                count += 1
print(count)