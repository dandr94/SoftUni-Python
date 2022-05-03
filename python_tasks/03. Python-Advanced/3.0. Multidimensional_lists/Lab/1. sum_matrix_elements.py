rows, columns = [int(x) for x in input().split(', ')]

matrix = []
sum_result = 0

# List comp: matrix = [[int(num) for num in input().split(', ')] for i in range(rows)]

for i in range(rows):
    nums = [int(x) for x in input().split(', ')]
    matrix.append(nums)
    sum_result += sum(nums)


print(sum_result)
print(matrix)

