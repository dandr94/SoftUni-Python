def is_valid_position(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board[0]):
        return True
    return False


directions_dict = {
    1: lambda r, c: (r, c - 1),  # left
    2: lambda r, c: (r, c + 1),  # right
    3: lambda r, c: (r - 1, c),  # up
    4: lambda r, c: (r + 1, c),  # down
    5: lambda r, c: (r - 1, c - 1),  # left__up_diagonal
    6: lambda r, c: (r - 1, c + 1),  # right_up_diagonal
    7: lambda r, c: (r + 1, c - 1),  # left_down_diagonal
    8: lambda r, c: (r + 1, c + 1)  # right_down__diagonal
}
rows = 8
columns = 8

matrix = [[x for x in input().split()] for _ in range(rows)]

king_row = 0
king_col = 0

all_queens = []

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 'K':
            king_row = row
            king_col = col
        elif matrix[row][col] == 'Q':
            all_queens.append([row, col])

queens_list = []

for row, col in all_queens:
    for i in range(1, len(directions_dict) + 1):
        current_row = row
        current_col = col
        while True:
            step = directions_dict[i]
            next_row, next_col = step(current_row, current_col)

            if is_valid_position(matrix, next_row, next_col):
                if matrix[next_row][next_col] == 'K':
                    queens_list.append([row, col])
                    break
                elif matrix[next_row][next_col] == 'Q':
                    break

                current_row, current_col = next_row, next_col
            else:
                break

if queens_list:
    [print(x) for x in queens_list]
else:
    print('The king is safe!')
