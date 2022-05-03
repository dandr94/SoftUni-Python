def is_outside_of_matrix(row, col, size):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False


def next_position(dir, row, col):
    if dir == 'up':
        return row - 1, col
    if dir == 'down':
        return row + 1, col
    if dir == 'left':
        return row, col - 1
    return row, col + 1


n = int(input())

matrix = [[x for x in input().split()] for _ in range(n)]
tea_bags_collected = 0
alice_row = 0
alice_col = 0
is_found = False

while True:
    if is_found:
        break
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 'A':
                alice_row = r
                alice_col = c
                is_found = True

matrix[alice_row][alice_col] = '*'

while True:
    cmd = input()
    alice_row, alice_col = next_position(cmd, alice_row, alice_col)

    if is_outside_of_matrix(alice_row, alice_col, len(matrix)):
        break

    curr_value = matrix[alice_row][alice_col]
    matrix[alice_row][alice_col] = '*'

    if curr_value == 'R':
        break
    if curr_value.isdigit():
        tea_bags_collected += int(curr_value)

        if tea_bags_collected >= 10:
            break

if tea_bags_collected >= 10:
    print(f'She did it! She went to the party.')
else:
    print(f"Alice didn't make it to the tea party.")

for i in matrix:
    print(" ".join(i))
