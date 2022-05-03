number = int(input())


sum = 0

num = int(input())

while sum <= number:
    sum += num
    if sum >= number:
        print(sum)
        break
    num = int(input())


