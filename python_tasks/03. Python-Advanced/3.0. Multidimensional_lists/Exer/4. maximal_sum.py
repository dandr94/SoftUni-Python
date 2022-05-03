rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

maximal_sum = 0
best_row = 0
best_column = 0

r = len(matrix)
c = len(matrix[0])

for row in range(r - 2):
    for column in range(c - 2):
        sum_of_squares = matrix[row][column] + \
                         matrix[row][column + 1] + \
                         matrix[row][column + 2] + \
                         matrix[row + 1][column] + \
                         matrix[row + 1][column + 1] + \
                         matrix[row + 1][column + 2] + \
                         matrix[row + 2][column] + \
                         matrix[row + 2][column + 1] + \
                         matrix[row + 2][column + 2]

        if sum_of_squares > maximal_sum:
            maximal_sum = sum_of_squares
            best_row = row
            best_column = column

print(f'Sum = {maximal_sum}')
print(matrix[best_row][best_column], matrix[best_row][best_column + 1], matrix[best_row][best_column + 2])
print(matrix[best_row + 1][best_column], matrix[best_row + 1][best_column + 1], matrix[best_row + 1][best_column + 2])
print(matrix[best_row + 2][best_column], matrix[best_row + 2][best_column + 1], matrix[best_row + 2][best_column + 2])



