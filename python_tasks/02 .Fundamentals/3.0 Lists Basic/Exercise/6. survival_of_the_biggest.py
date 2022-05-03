list_of_nums = input().split(' ')
n = int(input())
str_to_int_list = list(map(int, list_of_nums))

for i in range(1, n + 1):
    str_to_int_list.remove(min(str_to_int_list))

string_of_nums = ', '.join([str(final) for final in str_to_int_list])
print(string_of_nums)