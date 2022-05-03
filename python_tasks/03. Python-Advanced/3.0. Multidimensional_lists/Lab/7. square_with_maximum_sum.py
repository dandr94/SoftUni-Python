rows, columns = [int(x) for x in input().split(', ')]
#        0, 1, 2, 3, 4, 5
grid = [[7, 1, 3, 3, 2, 1],  # 0
        [1, 3, 9, 8, 5, 6],  # 1
        [4, 6, 7, 9, 1, 0]]  # 2

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

r = len(matrix)
c = len(matrix[0])

max_square = []
max_sum = 0

for i in range(r - 1):
    for j in range(c - 1):
        x = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if x > max_sum:
            max_sum = x
            max_square = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]


for sqr in max_square:
    print(' '.join(str(x) for x in sqr))
print(max_sum)