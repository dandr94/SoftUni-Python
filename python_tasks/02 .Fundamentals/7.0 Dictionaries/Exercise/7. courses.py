courses = {}

cmd = input()

while cmd != 'end':
    cmd_split = cmd.split(' : ')
    course = cmd_split[0]
    name = cmd_split[1]

    if course not in courses:
        courses[course] = []
    courses[course].append(name)

    cmd = input()

final = sorted(courses.items(), key=lambda x: len(x[1]), reverse=True)

for key, value in final:
    print(f'{key}: {len(value)}')
    for i in sorted(value):
        print(f'-- {i}')