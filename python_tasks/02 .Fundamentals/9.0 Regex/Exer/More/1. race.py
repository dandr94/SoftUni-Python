import re

list_of_people = input().split(', ')

my_dict = {}

for i in list_of_people:
    if i not in my_dict:
        my_dict[i] = 0

pattern = r'[A-Za-z0-9]'

cmd = input()

while cmd != 'end of race':
    name = ''
    num = 0

    result = re.finditer(pattern, cmd)

    for i in result:
        if i.group().isnumeric():
            num += int(i.group())
        else:
            name += i.group()

    if name in my_dict:
        my_dict[name] += num

    cmd = input()

count = 1
end = ''
for key, value in sorted(my_dict.items(), key=lambda x: -x[1]):
    if count == 1:
        end = 'st'
    elif count == 2:
        end = 'nd'
    else:
        end = 'rd'
    print(f'{count}{end} place: {key}')
    count += 1
    if count == 4:
        break
