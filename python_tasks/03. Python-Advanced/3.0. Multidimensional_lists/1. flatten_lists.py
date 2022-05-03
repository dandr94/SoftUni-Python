txt = input().split('|')

matrix = []

for index in range(len(txt) - 1, - 1, -1):
    el = txt[index].split()
    matrix += el

print(' '.join(matrix))