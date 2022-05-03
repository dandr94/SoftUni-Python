n = int(input())


result = 0
move_1 = 0
move_2 = 0
move_3 = 0
move_4 = 0
move_5 = 0
move_6 = 0

for i in range(1, n +1):
    moves = int(input())

    if moves >= 0 and moves <= 9:
        result += moves * 0.20
        move_1 += 1

    elif moves >= 10 and moves <= 19:
        result += moves * 0.30
        move_2 += 1

    elif moves >= 20 and moves <= 29:
        result += moves * 0.40
        move_3 += 1

    elif moves >= 30 and moves <= 39:
        result += 50
        move_4 += 1

    elif moves >= 40 and moves <= 50:
        result += 100
        move_5 += 1

    else:
        result /= 2
        move_6 += 1


percent_move_1 = move_1 / n * 100
percent_move_2 = move_2 / n * 100
percent_move_3 = move_3 / n * 100
percent_move_4 = move_4 / n * 100
percent_move_5 = move_5 / n * 100
percent_move_6 = move_6 / n * 100

print(f'{result:.2f}')
print(f'From 0 to 9: {percent_move_1:.2f}%')
print(f'From 10 to 19: {percent_move_2:.2f}%')
print(f'From 20 to 29: {percent_move_3:.2f}%')
print(f'From 30 to 39: {percent_move_4:.2f}%')
print(f'From 40 to 50: {percent_move_5:.2f}%')
print(f'Invalid numbers: {percent_move_6:.2f}%')