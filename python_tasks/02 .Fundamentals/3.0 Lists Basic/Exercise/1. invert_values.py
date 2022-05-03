some_string = input().split(' ')

result = list(map(int, some_string))
filtered = []

for number in result:
    if number > 0:
        filtered.append(-number)
    elif number < 0:
        filtered.append(abs(number))
    else:
        filtered.append(number)

print(filtered)

# opposite number can be done with multiple by -1 ( -1 * -1 = 1, 1 * -1 = -1)
