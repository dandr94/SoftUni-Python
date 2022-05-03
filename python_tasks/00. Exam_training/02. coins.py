from math import floor


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

rows = int(input())

matrix = [[x for x in input().split()] for _ in range(rows)]

player_row = 0
player_col = 0

my_path = []
coins = 0
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 'P':
            player_row = row
            player_col = col

while coins < 100:
    direction = input()

    step = directions_dict[direction]

    next_row, next_col = step(player_row, player_col)

    if is_valid_position(matrix, next_row, next_col):
        if matrix[next_row][next_col].isdigit():
            coins += int(matrix[next_row][next_col])
            my_path.append([next_row, next_col])

        elif matrix[next_row][next_col] == 'X':
            coins /= 2
            break

    else:
        coins /= 2
        break

    player_row, player_col = next_row, next_col

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {floor(coins)} coins.")

print('Your path:')
for cords in my_path:
    print(cords)
