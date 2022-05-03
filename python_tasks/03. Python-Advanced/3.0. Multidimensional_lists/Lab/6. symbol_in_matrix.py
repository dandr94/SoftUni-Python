n = int(input())

matrix = [[x for x in input()] for _ in range(n)]


needed_char = input()
found = False

for i in range(n):
    if found:
        break
    for j in range(len(matrix[i])):
        current = matrix[i][j]
        if matrix[i][j] == needed_char:
            print(f'({i}, {j})')
            found = True
            break

if not found:
    print(f'{needed_char} does not occur in the matrix')

