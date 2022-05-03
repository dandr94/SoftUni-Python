def is_valid_position(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board[0]):
        return True
    return False


def surrounding(board, r, c):
    result = 0

    if is_valid_position(board, r, c + 1) and matrix[r][c + 1] == '*':  # right
        result += 1
    if is_valid_position(board, r, c - 1) and matrix[r][c - 1] == '*':  # left
        result += 1
    if is_valid_position(board, r + 1, c) and matrix[r + 1][c] == '*':  # down
        result += 1
    if is_valid_position(board, r - 1, c) and matrix[r - 1][c] == '*':  # up
        result += 1
    if is_valid_position(board, r - 1, c - 1) and matrix[r - 1][c - 1] == '*':  # top_left_diagonal
        result += 1
    if is_valid_position(board, r - 1, c + 1) and matrix[r - 1][c + 1] == '*':  # top_right_diagonal
        result += 1
    if is_valid_position(board, r + 1, c - 1) and matrix[r + 1][c - 1] == '*':  # bottom_left_diagonal
        result += 1
    if is_valid_position(board, r + 1, c + 1) and matrix[r + 1][c + 1] == '*':  # bottom_right_diagonal
        result += 1

    return result


n = int(input())
bombs_need_to_place = int(input())

matrix = [[None for x in range(n)] for _ in range(n)]

for i in range(bombs_need_to_place):
    row, col = [int(x) for x in input()[1:-1].split(', ')]

    matrix[row][col] = '*'


for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] != '*':
            matrix[row][col] = surrounding(matrix, row, col)

for row in matrix:
    print(" ".join([str(x) for x in row]))