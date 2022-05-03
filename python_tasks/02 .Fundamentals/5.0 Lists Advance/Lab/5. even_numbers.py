numbers = input().split(', ')
numbers_to_int = list(map(int, numbers))
even_indexes = []

for i in range(len(numbers)):
    if numbers_to_int[i] % 2 == 0:
        even_indexes.append(i)

print(even_indexes)