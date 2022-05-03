number_of_matrix = int(input())

matrix = [[int(num) for num in input().split(', ') if int(num) % 2 == 0] for i in range(number_of_matrix)]

print(matrix)

