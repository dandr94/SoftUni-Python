contest_dict = {}
contest_points = {}
while True:
    some_cmd_str = input().split(':')

    if some_cmd_str[0] == 'end of contests':
        break

    contest_str = some_cmd_str[0]
    password_str = some_cmd_str[1]

    if contest_str not in contest_dict:
        contest_dict[contest_str] = password_str


while True:
    some_cmd = input().split('=>')

    if some_cmd[0] == 'end of submissions':
        break

    contest = some_cmd[0]
    password = some_cmd[1]
    username = some_cmd[2]
    points = int(some_cmd[3])

    if contest not in contest_dict:
        continue

    if contest_dict[contest] != password:
        continue

    if username not in contest_points:
        contest_points[username] = {}
        contest_points[username][contest] = points

    elif username in contest_points and contest in contest_points[username].keys():
        if points > contest_points[username][contest]:
            contest_points[username][contest] = points
    else:
        contest_points[username][contest] = points


winner = ''
points_win = 0

for key, value in contest_points.items():
    sum_points = 0
    for num in value.values():
        sum_points += num

    if sum_points > points_win:
        points_win = sum_points
        winner = key

print(f'Best candidate is {winner} with total {points_win} points.')
print('Ranking:')
for key, value in sorted(contest_points.items(), key=lambda x: x[0]):
    print(f'{key}')
    for cont, con_points in sorted(value.items(), key=lambda x: -x[1]):
        print(f'#  {cont} -> {con_points}')
