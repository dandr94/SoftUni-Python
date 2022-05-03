list_of_things = input().split(', ')
for zeros in list_of_things:
    if zeros == '0':
        list_of_things.append(list_of_things.pop(list_of_things.index(zeros)))

result = list(map(int, list_of_things))
print(result)
