num_divisor = int(input())
num_bound = int(input())

num = 0

for i in range(1, num_bound + 1):

    if i % num_divisor == 0:
        if i > num:
            num = i


print(num)