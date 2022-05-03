def is_valid_position(r, c, row, column):
    return 0 <= row < r and 0 <= column < c


n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

r = len(matrix)
c = len(matrix[0])

while True:
    cmd = input().split()

    if cmd[0] == 'END':
        break

    row, col, value = [int(x) for x in cmd[1:]]

    if is_valid_position(r, c, row, col):

        if cmd[0] == 'Add':
            matrix[row][col] += value

        elif cmd[0] == 'Subtract':
            matrix[row][col] -= value

    else:
        print('Invalid coordinates')

for i in matrix:
    print(' '.join(str(x) for x in i))
