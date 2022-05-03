string_of_numbers = input().split(' ')
string_with_chars = input()

count = 0
my_list = []
my_numbers = []
sum_num = 0
result = []
for i in string_with_chars:
    my_list.append(i)
for b in string_of_numbers:
    for c in b:
        sum_num += int(c)
    my_numbers.append(sum_num)
    sum_num = 0

for index in my_numbers:
    while count != index:
        for length in my_list:
            if count == index:
                result.append(my_list.pop(my_list.index(length)))
                break
            else:
                count += 1

    count = 0

final_result = ''.join(result)
print(final_result)






