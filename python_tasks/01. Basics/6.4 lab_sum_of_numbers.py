first_num = int(input())
second_num = int(input())
magic_number = int(input())
count = 0


for i in range(first_num, second_num + 1):
    for n in range(first_num, second_num + 1):
        count += 1
        if i + n == magic_number:
            print(f'Combination N:{count} ({i} + {n} = {magic_number})')
            quit()

print(f'{count} combinations - neither equals {magic_number}')