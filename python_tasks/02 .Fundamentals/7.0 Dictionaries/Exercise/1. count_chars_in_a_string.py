list_of_things = input().split()

my_dict = {}

for i in list_of_things:
    for b in i:
        if b not in my_dict:
            my_dict[b] = 0

        my_dict[b] += 1

for key, value in my_dict.items():
    print(f'{key} -> {value}')