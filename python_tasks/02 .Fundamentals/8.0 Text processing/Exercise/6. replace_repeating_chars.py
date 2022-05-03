some_string = input()

unique_char = ''


for i in some_string:
    if i != unique_char:
        print(i, end='')
        unique_char = i
