def is_knight(chess_field, row, column):
    chess_size = len(chess_field)
    if row < 0 or column < 0 or row >= chess_size or column >= chess_size:
        return False
    return chess_field[row][column] == 'K'


def affected_knights(chess_field, row, column):
    result = 0
    if is_knight(chess_field, row - 2, column - 1):
        result += 1
    if is_knight(chess_field, row - 2, column + 1):
        result += 1
    if is_knight(chess_field, row + 2, column - 1):
        result += 1
    if is_knight(chess_field, row + 2, column + 1):
        result += 1
    if is_knight(chess_field, row - 1, column - 2):
        result += 1
    if is_knight(chess_field, row - 1, column + 2):
        result += 1
    if is_knight(chess_field, row + 1, column - 2):
        result += 1
    if is_knight(chess_field, row + 1, column + 2):
        result += 1
    return result


n = int(input())

matrix = [[x for x in input()] for _ in range(n)]

knights_removed = 0

while True:
    max_affected = 0
    max_row = 0
    max_col = 0

    for r in range(n):
        for c in range(n):
            if matrix[r][c] == '0':
                continue
            curr_affected = affected_knights(matrix, r, c)
            if curr_affected > max_affected:
                max_affected = curr_affected
                max_row = r
                max_col = c
    if max_affected == 0:
        break

    matrix[max_row][max_col] = '0'
    knights_removed += 1

print(knights_removed)
