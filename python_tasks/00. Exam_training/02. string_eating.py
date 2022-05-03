def is_valid_position(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board[0]):
        return True
    return False


directions_dict = {
    'left': lambda r, c: (r, c - 1),  # left
    'right': lambda r, c: (r, c + 1),  # right
    'up': lambda r, c: (r - 1, c),  # up
    'down': lambda r, c: (r + 1, c),  # down
}

my_string = input()
rows = int(input())
matrix = [[x for x in input()] for _ in range(rows)]
quantity_commands = int(input())

player_row = 0
player_col = 0

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 'P':
            player_row = row
            player_col = col

for i in range(quantity_commands):
    way = input()

    step = directions_dict[way]

    next_row, next_col = step(player_row, player_col)

    if is_valid_position(matrix, next_row, next_col):
        if matrix[next_row][next_col].isalpha():
            my_string += matrix[next_row][next_col]

        matrix[player_row][player_col] = '-'
        player_row, player_col = next_row, next_col
        matrix[player_row][player_col] = 'P'
    else:
        if my_string:
            my_string = my_string[:-1]

print(my_string)
for row in matrix:
    print(''.join(row))