# with open('text.txt', 'w') as txt:
#     txt.write("-I was quick to judge him, but it wasn't his fault.\n")
#     txt.write("-Is this some kind of joke?! Is it?\n")
#     txt.write("-Quick, hide here. It is safer.")

import re

with open('text.txt') as file:
    lines = file.readlines()

for index, line in enumerate(lines):

    if index % 2 != 0:
        continue

    line = re.sub(r'[-,.!?]', '@', line)  # sub replaces all matching elements with the second argument
    line = ' '.join(line.split()[::-1])

    print(line)
