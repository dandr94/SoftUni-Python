n_1 = int(input())
n_2 = int(input())
n_3 = int(input())


for num_1 in range(1, n_1 + 1):
    if num_1 % 2 == 0:
        for num_2 in range(2, n_2 + 1):
            for num_2_prime in range(2, num_2):
                if num_2 % num_2_prime == 0:
                    break
            else:
                for num_3 in range(1, n_3 + 1):
                    if num_3 % 2 == 0:
                        print(f'{num_1} {num_2 } {num_3}')