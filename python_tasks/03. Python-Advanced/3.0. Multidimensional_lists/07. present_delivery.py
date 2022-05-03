def is_outside(r, c, board_size):
    if r < 0 or c < 0 or r >= board_size or c >= board_size:
        return True
    return False


def valid_next_position(dir, r, c,):
    if dir == 'up':
        return r - 1, c
    if dir == 'down':
        return r + 1, c
    if dir == 'left':
        return r, c - 1
    return r, c + 1


def houses_in_range(dir, r, c):
    houses = []
    if not is_outside(r - 1, c, dir):
        houses.append([r - 1, c])
    if not is_outside(r + 1, c, dir):
        houses.append([r + 1, c])
    if not is_outside(r, c - 1, dir):
        houses.append([r, c - 1])
    if not is_outside(r, c + 1, dir):
        houses.append([r, c + 1])
    return houses


presents = int(input())
size = int(input())

matrix = [[x for x in input().split()] for _ in range(size)]

santa_row = 0
santa_col = 0
starting_good_kids = 0

for i in range(size):
    for j in range(size):
        if matrix[i][j] == 'S':
            santa_row = i
            santa_col = j
        elif matrix[i][j] == 'V':
            starting_good_kids += 1

good_kids_count = starting_good_kids

while True:
    line = input()

    if line == 'Christmas morning':
        break

    next_santa_row, next_santa_col = valid_next_position(line, santa_row, santa_col)

    if matrix[next_santa_row][next_santa_col] == 'V':
        good_kids_count -= 1
        presents -= 1

    elif matrix[next_santa_row][next_santa_col] == 'C':
        in_range_of_a_house = houses_in_range(size, next_santa_row, next_santa_col)

        for row, col in in_range_of_a_house:
            if matrix[row][col] == 'X':
                presents -= 1
            if matrix[row][col] == 'V':
                presents -= 1
                good_kids_count -= 1
            matrix[row][col] = '-'
            if presents == 0:
                break

    matrix[santa_row][santa_col] = '-'
    matrix[next_santa_row][next_santa_col] = 'S'
    santa_row, santa_col = next_santa_row, next_santa_col

    if presents == 0:
        break
if presents == 0 and good_kids_count > 0:
    print('Santa ran out of presents!')

for rows in matrix:
    print(' '.join(rows))

if good_kids_count == 0:
    print(f'Good job, Santa! {starting_good_kids} happy nice kid/s.')
else:
    print(f'No presents for {good_kids_count} nice kid/s.')
