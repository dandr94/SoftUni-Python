def is_valid_position(r, c, row, column):
    return 0 <= r < row and 0 <= c < column


rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]

while True:
    cmd = input()

    if cmd == 'END':
        break

    cmd_split = cmd.split()

    if 'swap' not in cmd[0] and len(cmd_split[1:]) != 4:
        print('Invalid input!')
        continue
    row1, col1, row2, col2 = [int(x) for x in cmd_split[1:]]
    if not is_valid_position(row1, col1, rows, columns) or not is_valid_position(row2, col2, rows, columns):
        print('Invalid input!')
        continue
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for i in matrix:
        print(' '.join([str(x) for x in i]))
