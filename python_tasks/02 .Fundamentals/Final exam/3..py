followers = {}


cmd = input()

while cmd != 'Log out':
    cmd_split = cmd.split(': ')
    action = cmd_split[0]
    username = cmd_split[1]

    if action == 'New follower':
        if username not in followers:
            followers[username] = []
            followers[username].append(0)
            followers[username].append(0)

    elif action == 'Like':
        count = int(cmd_split[2])

        if username not in followers:
            followers[username] = []
            followers[username].append(count)
            followers[username].append(0)
        else:
            followers[username][0] += count

    elif action == 'Comment':

        if username not in followers:
            followers[username] = []
            followers[username].append(0)
            followers[username].append(1)
        else:
            followers[username][1] += 1

    elif action == 'Blocked':

        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")

    cmd = input()

final_dict = {}

for key, value in followers.items():
    final_dict[key] = sum(value)


print(f'{len(followers)} followers')
for key, value in sorted(final_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f'{key}: {value}')

