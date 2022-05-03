def is_valid_position(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board[0]):
        return True
    return False


row = int(input())
directions = [x for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(row)]

directions_dict = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

player_row = 0
player_col = 0

coal = 0

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 's':
            player_row = row
            player_col = col
        elif matrix[row][col] == 'c':
            coal += 1

last_position = ''

while directions:
    way = directions.pop(0)
    step = directions_dict[way]

    next_row, next_col = step(player_row, player_col)

    if is_valid_position(matrix, next_row, next_col):
        if matrix[next_row][next_col] == 'e':
            print(f'Game over! ({next_row}, {next_col})')
            directions.append(way)
            break

        elif matrix[next_row][next_col] == 'c':
            coal -= 1
            matrix[next_row][next_col] = '*'

        player_row, player_col = next_row, next_col

    if not coal:
        collected_all = True
        last_position = f'({player_row}, {player_col})'
        break

    last_position = f'({player_row}, {player_col})'

if not coal:
    print(f"You collected all coal! {last_position}")
elif not directions and coal:
    print(f"{coal} pieces of coal left. {last_position}")
