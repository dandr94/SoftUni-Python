n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_diagonal = []
secondary_diagonal = []

for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][- 1 - i])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
