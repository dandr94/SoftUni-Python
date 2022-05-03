import re

cmd = input()

while cmd:
    pattern = r'\d+'

    result = re.findall(pattern, cmd)
    if result:
        print(*result, end=' ')

    cmd = input()