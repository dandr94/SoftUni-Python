number_of_matrix = int(input())

matrix = [[int(x) for x in input().split(', ')] for i in range(number_of_matrix)]
flatness = [num for sublist in matrix for num in sublist]
print(flatness)