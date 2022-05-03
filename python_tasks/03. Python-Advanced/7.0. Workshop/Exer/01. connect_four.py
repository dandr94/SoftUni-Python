rows = 6
columns = 7

board = [[0 for x in range(columns)] for _ in range(rows)]

current_player, opponent = 1, 2

down = right = 1
left = up = -1
same = 0


def current_positions_in_direction(matrix, start_position, direction):
    start_row, start_col = start_position
    move_by_row, move_by_col = direction

    positions = []

    current_row, current_col = start_row, start_col


    for _ in range(3):
        current_row += move_by_row
        current_col += move_by_col

        if not 0 <= current_row < len(matrix):
            return positions
        if not 0 <= current_col < len(board[current_row]):
            return positions

        positions.append(matrix[current_row][current_col])



    return positions


def is_stalemate(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if col == 0:
                return False

    return True


def is_valid_placement(matrix, c):
    for row in range(0, rows):
        if matrix[row][c] != 0:
            return row - 1

    return rows - 1


# def winning_move(matrix, last_position):
#     directions = [
#         ('right', (same, right)),
#         ('down,right', (down, right)),
#         ('down', (down, same)),
#         ('down_left', (down, left)),
#         ('left', (same, left)),
#         ('up_left', (up, left)),
#         ('up_right', (up, right))
#     ]
#
#     last_row, last_col = last_position
#
#     for _, direction in directions:
#         positions = current_positions_in_direction(matrix, last_position, direction)
#
#         if len(positions) == 4 and all([pos == board[last_row][last_col] for pos in positions]):
#             return True
#
#     return False


def has_four_consecutive(target_line, target):
    count = 0
    for el in target_line:
        if el == target:
            count += 1
        else:
            count = 0

        if count == 4:
            return True

    return False


def winning_move(matrix, last_position):
    left_horizontal = same, left
    right_horizontal = same, right
    up_vertical = up, same
    down_vertical = down, same
    up_right_diagonal = up, right
    up_left_diagonal = up, left
    down_left_diagonal = down, left
    down_right_diagonal = down, right

    directions = [
        (left_horizontal, right_horizontal),
        (up_vertical, down_vertical),
        (up_right_diagonal, down_left_diagonal),
        (up_left_diagonal, down_right_diagonal),
    ]

    start_row, start_col = last_position

    for backwards_dir, forward_dir in directions:
        backwards_pos = current_positions_in_direction(board, last_position, backwards_dir)
        forward_pos = current_positions_in_direction(board, last_position, forward_dir)

        target_line = list(reversed(backwards_pos)) + [matrix[start_row][start_col]] + forward_pos

        if has_four_consecutive(target_line, target=matrix[start_row][start_col]):
            return True

    return False


while True:
    try:
        print(f'Player {current_player} select a column')
        column_choice = int(input())
    except ValueError:
        continue
    column_choice -= 1

    if not 0 <= column_choice < columns:
        continue

    row = is_valid_placement(board, column_choice)

    if row == -1:
        continue

    board[row][column_choice] = current_player

    if is_stalemate(board):
        print('Stalemate. Game over!')
        break

    if winning_move(board, (row, column_choice)):
        print(f'Player {current_player} won!')
        break

    for i in board:
        print(i)
    current_player, opponent = opponent, current_player
