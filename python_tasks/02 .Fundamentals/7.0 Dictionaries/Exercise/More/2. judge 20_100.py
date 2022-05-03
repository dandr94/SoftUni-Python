part_dict = {}
test_doct = {}
while True:
    some_cmd = input().split(' -> ')

    if some_cmd[0] == 'no more time':
        break

    username = some_cmd[0]
    contest = some_cmd[1]
    points = int(some_cmd[2])

    if contest not in part_dict:
        part_dict[contest] = {}
        part_dict[contest][username] = points
    elif contest in part_dict and username in part_dict.keys():
        if points > part_dict[contest][username]:
            part_dict[contest][username] = points
    else:
        part_dict[contest][username] = points


for key, value in sorted(part_dict.items(), key=lambda x: len(x[1]), reverse=True):
    print(f'{key}: {len(value)} participants')
    count = 1
    for name, points in sorted(value.items(), key=lambda x: -x[1]):
        print(f'{count}. {name} <::> {points}')
        count += 1

print('Individual standings:')

invid_dict = {}

for key, value in part_dict.items():
    for name, points in value.items():
        if name not in invid_dict:
            invid_dict[name] = points
        else:
            invid_dict[name] += points

count = 1
for key, value in sorted(invid_dict.items(), key=lambda x: -x[1]):
    print(f'{count}. {key} -> {value}')
    count += 1

