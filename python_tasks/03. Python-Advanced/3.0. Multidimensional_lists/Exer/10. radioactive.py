def is_valid_position(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board[0]):
        return True
    return False


def not_alive(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if matrix[row][col] == 'P':
                return False

    return True


def spread_bunny(board, list_of_bunnies):
    for i in list_of_bunnies:
        row_bunny = i[0]
        col_bunny = i[1]
        if is_valid_position(board, row_bunny, col_bunny + 1):
            board[row_bunny][col_bunny + 1] = 'B'
        if is_valid_position(board, row_bunny, col_bunny - 1):
            board[row_bunny][col_bunny - 1] = 'B'
        if is_valid_position(board, row_bunny - 1, col_bunny):
            board[row_bunny - 1][col_bunny] = 'B'
        if is_valid_position(board, row_bunny + 1, col_bunny):
            board[row_bunny + 1][col_bunny] = 'B'


directions_dict = {
    'R': lambda r, c: (r, c + 1),
    'L': lambda r, c: (r, c - 1),
    'U': lambda r, c: (r - 1, c),
    'D': lambda r, c: (r + 1, c),
}

rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input()] for _ in range(rows)]
directions = [x for x in input()]
player_row = 0
player_col = 0

bunnies = []

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 'P':
            player_row = row
            player_col = col
        elif matrix[row][col] == 'B':
            bunnies.append([row, col])

survived = True

last_position = ''

for way in directions:
    step = directions_dict[way]

    next_row, next_col = step(player_row, player_col)

    if is_valid_position(matrix, next_row, next_col):
        if matrix[next_row][next_col] == '.':
            matrix[player_row][player_col] = '.'
            player_row, player_col = next_row, next_col
            matrix[player_row][player_col] = 'P'

        elif matrix[next_row][next_col] == 'B':
            survived = False

        spread_bunny(matrix, bunnies)

        if not_alive(matrix):
            survived = False

        if not survived:
            last_position = f'{next_row} {next_col}'
            break
    else:
        matrix[player_row][player_col] = '.'
        spread_bunny(matrix, bunnies)
        last_position = f'{player_row} {player_col}'
        break

    bunnies.clear()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'B':
                bunnies.append([row, col])
for row in matrix:
    print(''.join([str(x) for x in row]))

if survived:
    print(f'won: {last_position}')
else:
    print(f'dead: {last_position}')
