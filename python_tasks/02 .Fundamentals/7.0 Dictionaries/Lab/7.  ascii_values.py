list_of_things = input().split(', ')
x = {x: ord(x) for x in list_of_things}
print(x)