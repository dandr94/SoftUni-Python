import sys
n = int(input())

max_number = -sys.maxsize
sum = 0
for i in range(1, n + 1):
    num = int(input())
    if num > max_number:
        max_number = num
    sum += num
sum -= max_number

if sum == max_number:
    print('Yes')
    print(f'Sum = {sum}')
else:
    print('No')
    diff = max_number - sum
    print(f'Diff = {abs(diff)}')