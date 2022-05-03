from collections import deque

robots_rough = input().split(';')

robots = deque(x.split('-') for x in robots_rough)
print(robots)

my_dict = {}

time = input()

for i in robots:
    robot = i[0]
    time_work = i[1]

    if robot not in my_dict:
        my_dict[robot] = []

    my_dict[robot].append(time_work)
    my_dict[robot].append(time)

while True:
    cmd = input()

    if cmd == 'End':
        break

