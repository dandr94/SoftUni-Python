n = int(input())


odd = 0
even = 0

for i in range(1, n+1):
    number = int(input())
    if i % 2 == 0:
        even += number
    else:
        odd += number

if odd == even:
    print('Yes')
    print(f'Sum = {odd}')
else:
    diff = odd - even
    print('No')
    print(f'Diff = {abs(diff)}')