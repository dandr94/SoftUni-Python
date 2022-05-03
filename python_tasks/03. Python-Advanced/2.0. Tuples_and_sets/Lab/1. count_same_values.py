tuples = tuple(map(float, input().split()))

count_of_tuples = {}

for i in tuples:
    if i not in count_of_tuples:
        count_of_tuples[i] = 1
    else:
        count_of_tuples[i] += 1

for key, value in count_of_tuples.items():
    print(f'{key} - {value} times')
