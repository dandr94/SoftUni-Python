start_value_first_pair = int(input())
start_value_second_pair = int(input())
difference_first_pair = int(input())
difference_second_pair = int(input())

for a in range(start_value_first_pair, start_value_first_pair + difference_first_pair + 1):
    for is_a_prime in range(2, a):
        if a % is_a_prime == 0:
            break
    else:
        for b in range(start_value_second_pair, start_value_second_pair + difference_second_pair + 1):
            for is_b_prime in range(2, b):
                if b % is_b_prime == 0:
                    break
            else:
                print(f'{a}{b}')


