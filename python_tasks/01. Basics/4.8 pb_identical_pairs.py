n = int(input())

prev_sum = 0
sum = 0
highest_diff = 0

for i in range(1, n +1):
    if i == 1:
        num_1 = int(input())
        num_2 = int(input())
        prev_sum = num_1 + num_2

    else:
        num_1 = int(input())
        num_2 = int(input())

        sum = num_1 + num_2

        if abs(sum - prev_sum) > highest_diff:
            highest_diff = abs(sum - prev_sum)

        prev_sum = sum

if highest_diff > 0:
    print(f'No, maxdiff={highest_diff}')
else:
    print(f'Yes, value={prev_sum}')







