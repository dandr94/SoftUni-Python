def is_outside(r, c, board_size):
    if r < 0 or c < 0 or r >= board_size or c >= board_size:
        return True
    return False


def valid_next_position(dir, r, c, step):
    if dir == 'up':
        return r - step, c
    if dir == 'down':
        return r + step, c
    if dir == 'left':
        return r, c - step
    return r, c + step


n = 5

matrix = [[x for x in input().split()] for _ in range(n)]

number_of_cmd = int(input())

player_row = 0
player_col = 0
all_targets = 0
hits = 0
targets_positions = []

target_direction = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'A':
            player_row = i
            player_col = j
        elif matrix[i][j] == 'x':
            all_targets += 1

for commands in range(number_of_cmd):
    cmd = input().split()
    direction = cmd[1]

    if cmd[0] == 'move':
        steps = int(cmd[2])
        future_player_row, future_player_col = valid_next_position(direction, player_row, player_col, steps)

        if is_outside(future_player_row, future_player_col, n):
            continue

        if matrix[future_player_row][future_player_col] != '.':
            continue

        matrix[player_row][player_col] = '.'
        matrix[future_player_row][future_player_col] = 'A'
        player_row, player_col = future_player_row, future_player_col

    elif cmd[0] == 'shoot':
        step = target_direction[direction]
        shoot_row, shoot_col = step(player_row, player_col)

        while True:
            if is_outside(shoot_row, shoot_col, n):
                break

            if matrix[shoot_row][shoot_col] == 'x':
                hits += 1
                matrix[shoot_row][shoot_col] = '.'
                targets_positions.append([shoot_row, shoot_col])
                break

            shoot_row, shoot_col = step(shoot_row, shoot_col)

        if hits == all_targets:
            break

if hits == all_targets:
    print(f'Training completed! All {hits} targets hit.')
else:
    print(f'Training not completed! {all_targets - hits} targets left.')

for pos in targets_positions:
    print(pos)