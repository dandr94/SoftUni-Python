def is_valid_position(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board[0]):
        return True
    return False


directions_dict = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

rows = 6
columns = 6

matrix = [[x for x in input().split()] for _ in range(rows)]
points = 0

for _ in range(3):
    row, col = [int(x) for x in input()[1:-1].split(', ')]

    if is_valid_position(matrix, row, col):
        if matrix[row][col] == 'B':
            for num in range(len(matrix)):
                if matrix[num][col].isdigit():
                    points += int(matrix[num][col])
            matrix[row][col] = '.'

if 100 <= points < 200:
    print(f'Good job! You scored {points} points, and you\'ve won Football.')
elif 200 <= points < 300:
    print(f'Good job! You scored {points} points, and you\'ve won Teddy Bear.')
elif points >= 300:
    print(f'Good job! You scored {points} points, and you\'ve won Lego Construction Set.')
else:
    print(f'Sorry! You need {100 - points} points more to win a prize.')
