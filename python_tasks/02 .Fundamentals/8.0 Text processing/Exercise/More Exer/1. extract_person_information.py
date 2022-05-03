n = int(input())

my_dict = {}
flag_name = False
flag_age = False

for i in range(n):
    some_string = input()
    name = ''
    age = ''

    for b in some_string:
        if b == '@':
            flag_name = True
            continue
        elif b == '|':
            flag_name = False
        elif b == '#':
            flag_age = True
            continue
        elif b == '*':
            flag_age = False

        if flag_name:
            name += b
        if flag_age:
            age += b

    else:
        if name not in my_dict:
            my_dict[name] = age


for name, age in my_dict.items():
    print(f'{name} is {age} years old.')