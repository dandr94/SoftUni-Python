first_num = int(input())
second_num = int(input())
third_num = int(input())

if second_num < first_num > third_num:
    print(first_num)

elif first_num < second_num > third_num:
    print(second_num)

elif second_num < third_num > first_num:
    print(third_num)

# print(max(first_num, second_num, third_num))