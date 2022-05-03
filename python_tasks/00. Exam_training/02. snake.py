def is_valid_position(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board[0]):
        return True
    return False


n = int(input())

matrix = [[x for x in input()] for _ in range(n)]

snake_row = 0
snake_column = 0

for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        if matrix[row][column] == 'S':
            snake_row = row
            snake_column = column
            matrix[row][column] = '.'

directions_dict = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

food = 0

not_failed = True

while True:
    cmd = input()

    step = directions_dict[cmd]

    next_row, next_col = step(snake_row, snake_column)

    if is_valid_position(matrix, next_row, next_col):
        if matrix[next_row][next_col] == '*':
            food += 1
            if food == 10:
                matrix[next_row][next_col] = 'S'
                break
        elif matrix[next_row][next_col] == 'B':
            matrix[next_row][next_col] = '.'
            for row in range(len(matrix)):
                for column in range(len(matrix[0])):
                    if matrix[row][column] == 'B':
                        next_row = row
                        next_col = column

        snake_row, snake_column = next_row, next_col
        matrix[snake_row][snake_column] = '.'

    else:
        not_failed = False
        break

if not_failed:
    print('You won! You fed the snake.')
else:
    print('Game over!')

print(f'Food eaten: {food}')

for row in matrix:
    print(''.join(row))

