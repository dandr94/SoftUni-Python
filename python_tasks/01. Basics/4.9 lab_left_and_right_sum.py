n = int(input())


left_sum = 0
right_sum = 0

for i in range(1, n * 2 + 1):
    number = int(input())
    if i <= n:
        left_sum += number
    else:
        right_sum += number

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = left_sum - right_sum
    print(f'No, diff = {abs(diff)}')