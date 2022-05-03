rows, columns = [int(x) for x in input().split()]

matrix = []

string = [x for x in input()]

index_of_word = 0

for row in range(rows):
    matrix.append([None] * columns)
    for column in range(columns):
        if row % 2 == 0:
            matrix[row][column] = string[index_of_word]
        else:
            matrix[row][- 1 - column] = string[index_of_word]
        index_of_word = (index_of_word + 1) % len(string)


for i in matrix:
    print(''.join([x for x in i]))