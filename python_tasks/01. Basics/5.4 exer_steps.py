goal = 10_000

while goal > 0:
    steps = input()
    if steps == 'Going home':
        steps_to_home = int(input())
        goal -= steps_to_home
        break
    else:
        goal -= int(steps)

if goal > 0:
    print(f'{goal} more steps to reach goal.')
else:
    print('Goal reached! Good job!')
    print(f'{abs(goal)} steps over the goal!')
