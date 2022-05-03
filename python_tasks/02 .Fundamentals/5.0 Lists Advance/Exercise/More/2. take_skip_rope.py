string_of_letters_and_numbers = input()

list_of_nums = []
list_of_letters = []


for i in string_of_letters_and_numbers:
    if i.isdigit():
        list_of_nums.append(int(i))
    else:
        list_of_letters.append(i)

take_list = []
skip_list = []
better_list = []

for i in range(len(list_of_nums)):
    if i % 2 == 0:
        take_list.append(list_of_nums[i])
        better_list.append(list_of_nums[i])
    else:
        skip_list.append(list_of_nums[i])
        better_list.append(list_of_nums[i])

print(take_list)
print(skip_list)
print(better_list)

result_string = ''

for i in range(len(skip_list)):
    take = take_list[i]
    skip = skip_list[i]

    for b in range(0, take):
        result_string += list_of_letters[b]
        list_of_letters.pop(0)

    for c in range(0, skip):
        list_of_letters.pop(0)


