words = input().split()
dictionary = {}

for i in words:
    i_lower = i.lower()

    if i_lower not in dictionary:
        dictionary[i_lower] = 0

    dictionary[i_lower] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=' ')
