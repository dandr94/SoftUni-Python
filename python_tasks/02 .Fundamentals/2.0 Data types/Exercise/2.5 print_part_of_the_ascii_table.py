start = int(input())
end = int(input())

for i in range(start, end + 1):
    if i == end:
        print(f'{chr(i)}')
    else:
        print(f'{chr(i)}',end=' ')
