list_of_numbers = input().split(', ')
list_to_int = list(map(int, list_of_numbers))

max_value = 10

while list_to_int:
    group_of_numbers = list(filter((lambda x: x <= max_value), list_to_int))
    print(f"Group of {max_value}'s: {group_of_numbers}")
    for i in group_of_numbers:
        if i in list_to_int:
            list_to_int.remove(i)
    max_value += 10