def is_bomb(r, c, index_list):
    for cord in index_list:
        cord_row = int(cord[0])
        cord_col = int(cord[2])
        if cord_row == r and cord_col == c:
            return True

    return False


def dead_cell(board, r, c):
    if board[r][c] <= 0:
        return True
    return False


def is_valid_position(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board[0]):
        return True
    return False


def deal_damage(board, r, c, damage, tup):
    if is_valid_position(board, r, c + 1) and not dead_cell(board, r, c + 1) and not is_bomb(r, c + 1, tup):  # right
        board[r][c + 1] -= damage
    if is_valid_position(board, r, c - 1) and not dead_cell(board, r, c - 1) and not is_bomb(r, c - 1, tup):  # left
        board[r][c - 1] -= damage
    if is_valid_position(board, r - 1, c) and not dead_cell(board, r - 1, c) and not is_bomb(r - 1, c, tup):  # up
        board[r - 1][c] -= damage
    if is_valid_position(board, r + 1, c) and not dead_cell(board, r + 1, c) and not is_bomb(r + 1, c, tup):  # down
        board[r + 1][c] -= damage
    if is_valid_position(board, r - 1, c - 1) and not dead_cell(board, r - 1, c - 1) and not is_bomb(r - 1, c - 1,
                                                                                                     tup):  # top_left
        board[r - 1][c - 1] -= damage
    if is_valid_position(board, r - 1, c + 1) and not dead_cell(board, r - 1, c + 1) and not is_bomb(r - 1, c + 1,
                                                                                                     tup):  # top_right
        board[r - 1][c + 1] -= damage
    if is_valid_position(board, r + 1, c - 1) and not dead_cell(board, r + 1, c - 1) and not is_bomb(r + 1, c - 1,
                                                                                                     tup):  # bottom_left
        board[r + 1][c - 1] -= damage
    if is_valid_position(board, r + 1, c + 1) and not dead_cell(board, r + 1, c + 1) and not is_bomb(r + 1, c + 1,
                                                                                                     tup):  # bottom_right
        board[r + 1][c + 1] -= damage


rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

indexes = [x for x in input().split()]

for i in indexes:
    row = int(i[0])
    col = int(i[2])
    bomb_damage = matrix[row][col]

    deal_damage(matrix, row, col, bomb_damage, indexes)
    matrix[row][col] = 0

alive_cells = []

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] > 0:
            alive_cells.append(matrix[row][col])

print(f'Alive cells: {len(alive_cells)}')
print(f'Sum: {sum(alive_cells)}')
for row in matrix:
    print(' '.join([str(x) for x in row]))
