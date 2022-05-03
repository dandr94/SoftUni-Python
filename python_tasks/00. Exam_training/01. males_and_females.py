from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:
    current_male = males.pop()
    if current_male < 1:
        continue
    current_female = females.popleft()
    if current_female < 1:
        males.append(current_male)
        continue

    if current_male % 25 == 0:
        if males:
            females.appendleft(current_female)
            males.pop()
            continue
    if current_female % 25 == 0:
        if females:
            males.append(current_male)
            females.popleft()
            continue

    if current_male == current_female:
        matches += 1
        continue
    else:
        if current_male - 2 > 0:
            males.append(current_male - 2)


print(f'Matches: {matches}')
if males:
    print(f'Males left: {", ".join([str(x) for x in males[::-1]])}')
else:
    print('Males left: none')
if females:
    print(f'Females left: {", ".join([str(x) for x in females])}')
else:
    print('Females left: none')