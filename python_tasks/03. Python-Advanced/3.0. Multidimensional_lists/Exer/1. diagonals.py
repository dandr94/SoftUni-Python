n = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]

primary_diagonal = []
secondary_diagonal = []

for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][- 1 - i])

print(f'Primary diagonal: {", ".join(map(str,primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(map(str,secondary_diagonal))}. Sum: {sum(secondary_diagonal)}')
