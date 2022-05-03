n = int(input())


first_num = 0
second_num = 0
count = 0

for num_1 in range(1, 9+ 1):
    for num_2 in range(1, 9 +1):
        for num_3 in range(1, 9 +1):
            for num_4 in range(1, 9+ 1):
                if (num_1 + num_2) == (num_3 + num_4):
                    if n % (num_1 + num_2) == 0:
                        print(f'{num_1}{num_2}{num_3}{num_4}', end=' ')