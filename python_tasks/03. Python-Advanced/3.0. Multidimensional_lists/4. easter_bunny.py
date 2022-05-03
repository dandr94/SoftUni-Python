import sys


def in_matrix(size, row, col):
    return 0 <= row < size and 0 <= col < size


n = int(input())

matrix = [[x for x in input().split()] for _ in range(n)]

directions = {
    'right': lambda row, col: (row, col + 1),
    'left': lambda row, col: (row, col - 1),
    'down': lambda row, col: (row + 1, col),
    'up': lambda row, col: (row - 1, col)
}

bunny_row = 0
bunny_col = 0
is_found = False
while True:
    if is_found:
        break
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 'B':
                bunny_row = r
                bunny_col = c
                is_found = True

maximum_eggs = -sys.maxsize
side = ''
direction_list = []

for direction, step in directions.items():
    curr_row = bunny_row
    curr_col = bunny_col
    current_eggs = 0
    curr_list = []

    while True:
        curr_row, curr_col = step(curr_row, curr_col)

        if not in_matrix(n, curr_row, curr_col):
            break

        if matrix[curr_row][curr_col] == 'X':
            break

        current_eggs += int(matrix[curr_row][curr_col])
        curr_list.append(f'{curr_row}, {curr_col}')

        if current_eggs > maximum_eggs:
            maximum_eggs = current_eggs
            side = direction
            direction_list = curr_list


print(side)
for i in direction_list:
    print(f'[{i}]')
print(maximum_eggs)
