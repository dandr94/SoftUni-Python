n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

sum_of_diagonal = 0

for i in range(n):
    sum_of_diagonal += matrix[i][i]

print(sum_of_diagonal)