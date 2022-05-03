first_line = input().split(' ')
second_line = input().split(' ')
third_line = input().split(' ')

winner = ''
# rows
row_1 = first_line[0] == first_line[1] == first_line[2] != '0'
row_2 = second_line[0] == second_line[1] == second_line[2] != '0'
row_3 = third_line[0] == third_line[1] == third_line[2] != '0'
# columns
column_1 = first_line[0] == second_line[0] == third_line[0] != '0'
column_2 = first_line[1] == second_line[1] == third_line[1] != '0'
column_3 = first_line[2] == second_line[2] == third_line[2] != '0'
# diagonals
diagonal_1 = first_line[0] == second_line[1] == third_line[2] != '0'
diagonal_2 = first_line[2] == second_line[1] == third_line[0] != '0'

if row_1:
    winner = first_line[0]
elif row_2:
    winner = second_line[0]
elif row_3:
    winner = third_line[0]
elif column_1:
    winner = first_line[0]
elif column_2:
    winner = first_line[1]
elif column_3:
    winner = first_line[2]
elif diagonal_1:
    winner = first_line[0]
elif diagonal_2:
    winner = first_line[2]

if winner == '1':
    print('First player won')
elif winner == '2':
    print('Second player won')
else:
    print('Draw!')