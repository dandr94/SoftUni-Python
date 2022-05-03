hundred = int(input())
decimal = int(input())
number = int(input())


for num_1 in range(1, hundred +1):
    if num_1 % 2 == 0:
        for num_2 in range(2, decimal + 1):
            if num_2 >= 0:
                for i in range(2, num_2):
                    if num_2 % i == 0:
                        break
                else:
                    for num_3 in range(1, number + 1):
                        if num_3 % 2 == 0:
                            print(f'{num_1} {num_2} {num_3}')
