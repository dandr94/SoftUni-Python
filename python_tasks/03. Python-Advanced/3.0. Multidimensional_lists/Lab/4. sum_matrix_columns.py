row, column = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split()] for _ in range(row)]

for i in range(column):
    size = 0
    for j in range(row):
        size += matrix[j][i]
    print(size)
