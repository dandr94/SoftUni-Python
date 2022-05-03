start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
count = 0
magic_number_found = False
for a in range(start_interval, end_interval + 1):
    for b in range(start_interval, end_interval + 1):
        count += 1
        if a + b == magic_number:
            magic_number_found = True
            break
    else:
        continue
    break
if magic_number_found:
    print(f'Combination N:{count} ({a} + {b} = {a + b})')
else:
    print(f'{count} combinations - neither equals {magic_number}')