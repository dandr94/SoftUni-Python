import re

n = int(input())

pattern = r'\|(?P<boss>[A-Z]{4,})\|\:\#(?P<name>[A-Za-z]+ {1}[A-Za-z]+)\#'

for i in range(n):
    cmd = input()

    matches = re.finditer(pattern, cmd)

    for match in matches:
        print(f'{match.group("boss")}, The {match.group("name")}')
        print(f'>> Strength: {len(match.group("boss"))}')
        print(f'>> Armor: {len(match.group("name"))}')
        break
    else:
        print('Access denied!')

