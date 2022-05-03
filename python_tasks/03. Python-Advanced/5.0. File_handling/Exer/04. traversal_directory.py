import os

_, _, files = next(os.walk(input()))

by_type = {}

for file in files:
    ext = file.split('.')[-1]
    if ext not in by_type:
        by_type[ext] = []

    by_type[ext].append(file)

with open(os.path.expanduser('~/Desktop/report.txt'), 'w') as output:
    for ext in sorted(by_type):
        files = sorted(by_type[ext])
        output.write(f'.{ext}\n')

        for file in files:
            output.write(f'- - - {file}\n')

