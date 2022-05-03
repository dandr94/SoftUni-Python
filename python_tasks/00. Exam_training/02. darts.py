def is_valid_position(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board[0]):
        return True
    return False


rows, columns = 7, 7

current_player, other_player = [x for x in input().split(', ')]
matrix = [[x for x in input().split()] for _ in range(rows)]

my_dict = {
    current_player: [501, 0],
    other_player: [501, 0]
}

while True:
    row, col = [int(x) for x in input()[1:-1].split(', ')]

    my_dict[current_player][1] += 1

    if is_valid_position(matrix, row, col):
        if matrix[row][col].isdigit():
            my_dict[current_player][0] -= int(matrix[row][col])

        elif matrix[row][col] == 'D':
            num_1, num_2, num_3, num_4 = matrix[row][-1], matrix[row][0], matrix[-1][col], matrix[0][col]
            sum_of_numbers = (int(num_1) + int(num_2) + int(num_3) + int(num_4)) * 2
            my_dict[current_player][0] -= sum_of_numbers

        elif matrix[row][col] == 'T':
            num_1, num_2, num_3, num_4 = matrix[row][-1], matrix[row][0], matrix[-1][col], matrix[0][col]
            sum_of_numbers = (int(num_1) + int(num_2) + int(num_3) + int(num_4)) * 3
            my_dict[current_player][0] -= sum_of_numbers

        elif matrix[row][col] == 'B':
            print(f'{current_player} won the game with {my_dict[current_player][1]} throws!')
            winner = current_player
            break

    if my_dict[current_player][0] <= 0:
        print(f'{current_player} won the game with {my_dict[current_player][1]} throws!')
        break

    current_player, other_player = other_player, current_player
