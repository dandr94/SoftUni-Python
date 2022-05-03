secret_message = input().split()

for i in secret_message:
    new_list = []
    num_as_string = []
    for b in i:
        new_list.append(b)

    while new_list[0].isdigit():
        num_as_string.append(new_list[0])
        new_list.pop(0)

    num = int(''.join(num_as_string))
    new_list.insert(0, chr(num))

    new_list[1], new_list[-1] = new_list[-1], new_list[1]

    print(''.join(new_list),end=' ')